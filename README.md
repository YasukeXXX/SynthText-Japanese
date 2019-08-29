# SynthText for (English + Japanese)
Code for generating synthetic text images as described in ["Synthetic Data for Text Localisation in Natural Images", Ankush Gupta, Andrea Vedaldi, Andrew Zisserman, CVPR 2016](http://www.robots.ox.ac.uk/~vgg/data/scenetext/) with support for japanese characters

## Output samples


**Synthetic Japanese Text Samples 1**

![Japanese example 1](results/sample1.png "Synthetic Japanese Text Samples 1")


**Synthetic Japanese Text Samples 2**

![Japanese example 2](results/sample2.png "Synthetic Japanese Text Samples 2")


**Synthetic Japanese Text Samples 3**

![Japanese example 3](results/sample3.png "Synthetic Japanese Text Samples 3")


**Synthetic Japanese Text Samples 4**

![Japanese example 4](results/sample4.png "Synthetic Japanese Text Samples 4")

## How to use this source

### Install dependencies

```
# For python
pip2 install -r requirements.txt
pip3 install -r requirements.txt

# For japanese
sudo apt-get install libmecab2 libmecab-dev mecab mecab-ipadic mecab-ipadic-utf8 mecab-utils
```

### Text and Font Preparation

- Put your text data and font as follow (just clone the repo)

```
data
├── dset.h5
├── fonts
│   ├── fontlist.txt                        : your font list
│   ├── ubuntu
│   ├── ubuntucondensed
│   ├── ubuntujapanese                      : your japanese font
│   └── ubuntumono
├── models
│   ├── char_freq.cp
│   ├── colors_new.cp
│   └── font_px2pt.cp
└── newsgroup
    └── newsgroup.txt                       : your text source
```

- You can generate random Japanese text by using the `random_generate_text.py` script:
```bash
python3 random_generate_text.py
```

- Then generate font model and char model
```
python2 invert_font_size.py
python2 update_freq.py

mv char_freq.cp data/models/
mv font_px2pt.cp data/models/
```
### Pre-processed Background Images Preparation

The 8,000 background images used in the paper, along with their segmentation and depth masks, have been uploaded here:
`http://www.robots.ox.ac.uk/~vgg/data/scenetext/preproc/<filename>`, where, `<filename>` can be:

- `imnames.cp` [180K]: names of filtered files, i.e., those files which do not contain text
- `bg_img.tar.gz` [8.9G]: compressed image files (more than 8000, so only use the filtered ones in imnames.cp). md5 hash: `3eac26af5f731792c9d95838a23b5047  bg_img.tar.gz`.
- `depth.h5` [15G]: depth maps. md5 hash: `af97f6e6c9651af4efb7b1ff12a5dc1b depth.h5`.
- `seg.h5` [6.9G]: segmentation maps. md5 hash: `1605f6e629b2524a3902a5ea729e86b2  seg.h5`.

Note: due to large size, `depth.h5` is also available for download as 3-part split-files of 5G each.
These part files are named: `depth.h5-00, depth.h5-01, depth.h5-02`. Download using the path above, and put them together using `cat depth.h5-0* > depth.h5`.

```bash
mkdir background
cd background
wget http://www.robots.ox.ac.uk/~vgg/data/scenetext/preproc/imnames.cp
wget http://www.robots.ox.ac.uk/~vgg/data/scenetext/preproc/bg_img.tar.gz
wget http://www.robots.ox.ac.uk/~vgg/data/scenetext/preproc/depth.h5
wget http://www.robots.ox.ac.uk/~vgg/data/scenetext/preproc/seg.h5
```

- Unzip the `bg_img.tar.gz` with this command `tar -xvzf bg_img.tar.gz`

- 

### Generating samples

```
python gen.py --viz --lang ENG/JPN
```

This script will generate random scene-text image samples and store them in an h5 file in `results/SynthText.h5`. If the `--viz` option is specified, the generated output will be visualized as the script is being run; omit the `--viz` option to turn-off the visualizations. If you want to visualize the results stored in  `results/SynthText.h5` later, run:

```
python visualize_results.py
```


### Further Information
Please refer to the paper for more information, or contact me (email address in the paper).

