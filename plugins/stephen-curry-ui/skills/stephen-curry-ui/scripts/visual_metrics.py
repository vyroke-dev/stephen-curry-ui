#!/usr/bin/env python3
"""Measure screenshot traits and pixel deltas; does not judge aesthetic quality.
Requires Pillow. Use same viewport/content state for meaningful comparisons.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from PIL import Image, ImageChops, ImageEnhance, ImageStat


def summarize(path: str, sample_size=300):
    with Image.open(path) as source:
        img=source.convert('RGB')
    sample=img.copy()
    sample.thumbnail((sample_size,sample_size))
    colors=sample.quantize(colors=6,method=Image.Quantize.MEDIANCUT)
    palette=colors.getpalette()
    count=sorted(colors.getcolors() or [],reverse=True)
    major=[]
    for n,index in count[:5]:
        rgb=tuple(palette[3*index:3*index+3])
        major.append({'color':'#%02X%02X%02X'%rgb,'share':round(n/(sample.width*sample.height),4)})
    gray=sample.convert('L')
    stats=ImageStat.Stat(gray)
    edges=0;tested=0
    px=gray.load()
    for y in range(gray.height-1):
        for x in range(gray.width-1):
            tested+=1
            if abs(px[x,y]-px[x+1,y])+abs(px[x,y]-px[x,y+1])>55:edges+=1
    return {'file':str(path),'size':list(img.size),'meanLuminance':round(stats.mean[0]/255,4),
            'luminanceStdev':round(stats.stddev[0]/255,4),'approxEdgeDensity':round(edges/max(tested,1),4),
            'sampleMajorColors':major,
            'interpretation':'Descriptive screenshot metrics only; animated, anti-aliased and font differences affect results.'}


def compare(a:str,b:str,diff_output:str|None=None):
    with Image.open(a) as im_a: left=im_a.convert('RGB')
    with Image.open(b) as im_b: right=im_b.convert('RGB')
    if left.size!=right.size:
        return {'comparable':False,'reason':'Images must have identical pixel dimensions','sizeA':list(left.size),'sizeB':list(right.size)}
    difference=ImageChops.difference(left,right)
    stats=ImageStat.Stat(difference)
    mean_abs=sum(stats.mean)/(3*255)
    histogram=difference.convert('L').histogram()
    fraction_nonzero=1-histogram[0]/(left.width*left.height)
    result={'comparable':True,'meanAbsoluteRGBDelta':round(mean_abs,5),'pixelFractionWithChange':round(fraction_nonzero,5),
            'note':'A difference is not necessarily a defect. Compare matched real states under identical fonts, viewport, time and assets.'}
    if diff_output:
        target=Path(diff_output);target.parent.mkdir(parents=True,exist_ok=True)
        ImageEnhance.Contrast(difference).enhance(3).save(target)
        result['diffImage']=str(target)
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('image',help='Actual site screenshot or authorized reference image')
    p.add_argument('--against',help='Image of same size for raw pixel comparison')
    p.add_argument('--diff-out',help='Optional highlighted diff image (requires --against)')
    p.add_argument('--out',help='Optional JSON report path')
    a=p.parse_args()
    if a.diff_out and not a.against:p.error('--diff-out requires --against')
    report={'snapshot':summarize(a.image)}
    if a.against:
        report['reference']=summarize(a.against)
        report['comparison']=compare(a.image,a.against,a.diff_out)
    output=json.dumps(report,ensure_ascii=False,indent=2)
    if a.out:
        dest=Path(a.out);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(output+'\n',encoding='utf-8')
        print('Wrote',dest)
    else:print(output)


if __name__=='__main__':main()
