# sparce = "Boxplot displaying the degradation results measured in LPIPS for the ``Reduced Image Set'' experiment. The Y-axis represents the LPIPS scores achieved, while the X-axis indicates the frequency of image selection (every 1/nth image) for inclusion in the training set. "
# gamma = "Boxplot displaying the degradation results measured in LPIPS for the ``Gamma Correction'' experiment. The Y-axis represents the LPIPS scores achieved, while the X-axis indicates the percent of training images adjusted through gamma correction. "
# noise = "Boxplot displaying the degradation results measured in LPIPS for the ``Image Noise'' experiment. The Y-axis represents the LPIPS scores achieved, while the X-axis indicates standard deviation of a Gaussian noise with mean = 0, added to the training images. "
# pos_noise = "Boxplot displaying the degradation results measured in LPIPS for the ``Positional Noise'' experiment. The Y-axis represents the LPIPS scores achieved, while the X-axis indicates standard deviation of a Gaussian noise with mean = 0, which are used to create transform matrices of noises, that are applied to the translation part of camera poses of training images. "
# orient_noise = "Boxplot displaying the degradation results measured in LPIPS for the ``Orientation Noise'' experiment. The Y-axis represents the LPIPS scores achieved, while the X-axis indicates standard deviation of a Gaussian noise with mean = 0. Sampled noise is used to create transform matrices of noise, that are applied to the orientation component of camera poses of training images. "
# pos_orient_noise = "Boxplot displaying the degradation results measured in LPIPS for the ``Combined Pose Noise'' experiment. The Y-axis represents the LPIPS scores achieved, while the X-axis indicates standard deviation of a Gaussian noise with mean = 0. Sampled noise is used to create transform matrices of noise, that are applied to the positional and orientational components of camera poses of training images. "
# pns_green_noise = "Boxplot displaying the degradation results measured in LPIPS for the ``Channel-specific Image Pepper and Salt Noise'' experiment for green color. The Y-axis represents the LPIPS scores achieved, while the X-axis indicates percent of pixels, that are corrupted by Pepper and Salt noise, meaning values of pixels for green color are either set to 0 or 255. "
# pns_red_noise = "Boxplot displaying the degradation results measured in LPIPS for the ``Channel-specific Image Pepper and Salt Noise'' experiment for red color. The Y-axis represents the LPIPS scores achieved, while the X-axis indicates percent of pixels, that are corrupted by Pepper and Salt noise, meaning values of pixels for red color are either set to 0 or 255. "
# pns_blue_noise = "Boxplot displaying the degradation results measured in LPIPS for the ``Channel-specific Image Pepper and Salt Noise'' experiment for blue color. The Y-axis represents the LPIPS scores achieved, while the X-axis indicates percent of pixels, that are corrupted by Pepper and Salt noise, meaning values of pixels for blue color are either set to 0 or 255. "
# saturation = "Boxplot displaying the degradation results measured in LPIPS for the ``Saturation Change'' experiment. The Y-axis represents the LPIPS scores achieved, while the X-axis indicates standard deviation of a Gaussian noise with mean = 1. Coefficient is sampled and multiplied with the saturaion channel of training images. "
# range = "Boxplot displaying the degradation results measured in LPIPS for the ``Range'' experiment. The Y-axis represents the LPIPS scores achieved, while The X-axis represents the selected height range for training images, labeled by $N$, where images from $N-10\%$ to $N\%$ of maximum height are used. "
# benchmark = "Results of reconstruction quality measured in LPIPS for the ``Benchmark'' experiment, where original dataset without any degradations is used. The Y-axis represents the LPIPS scores achieved. "

sparce = "Boxplot displaying the degradation results measured in LPIPS for the ``Reduced Image Set'' experiment."
gamma = "Boxplot displaying the degradation results measured in LPIPS for the ``Gamma Correction'' experiment."
noise = "Boxplot displaying the degradation results measured in LPIPS for the ``Image Noise'' experiment."
pos_noise = "Boxplot displaying the degradation results measured in LPIPS for the ``Positional Noise'' experiment."
orient_noise = "Boxplot displaying the degradation results measured in LPIPS for the ``Orientation Noise'' experiment."
pos_orient_noise = "Boxplot displaying the degradation results measured in LPIPS for the ``Combined Pose Noise'' experiment."
pns_green_noise = "Boxplot displaying the degradation results measured in LPIPS for the ``Channel-specific Image Pepper and Salt Noise'' experiment for green color."
pns_red_noise = "Boxplot displaying the degradation results measured in LPIPS for the ``Channel-specific Image Pepper and Salt Noise'' experiment for red color."
pns_blue_noise = "Boxplot displaying the degradation results measured in LPIPS for the ``Channel-specific Image Pepper and Salt Noise'' experiment for blue color."
saturation = "Boxplot displaying the degradation results measured in LPIPS for the ``Saturation Change'' experiment."
range = "Boxplot displaying the degradation results measured in LPIPS for the ``Range'' experiment."
benchmark = "Results of reconstruction quality measured in LPIPS for the ``Benchmark'' experiment, where original dataset without any degradations is used."

model_nerfacto = "Nerfacto model is used. "
model_ngp = "Instant-ngp model is used. "

opt_on = "Pose optimizer is enabled. "
opt_off = "Pose optimizer is disabled. "

stump = " Stump dataset is used. "
lego = " Lego dataset is used. "


    
def get_text(experiment):
    if 'every' in experiment:
        return sparce
    elif 'gamma' in experiment:
        return  gamma
    elif 'noise-std' in experiment:
        return noise
    elif 'pos' in experiment and 'orient' in experiment:
        return pos_orient_noise
    elif 'pos' in experiment:
        return pos_noise
    elif 'orient' in experiment:
        return orient_noise
    elif 'green' in experiment:
        return pns_green_noise
    elif 'red' in experiment:
        return pns_red_noise
    elif 'blue' in experiment:
        return pns_blue_noise
    elif 'satur' in experiment:
        return saturation
    elif 'range' in experiment:
        return range
    elif 'benchmark' in experiment:
        return benchmark
    else:
        return ''

# extracted = [re.search(r'[^ -]*$', string).group(0) for string in strings]
    
    
def get_model(experiment):
    if 'nerfacto' in experiment:
        return model_nerfacto
    elif 'ngp' in experiment:
        return model_ngp
    else:
        return ''
    
def get_opt(experiment):
    # if 'on' in experiment:
    #     return opt_on
    # elif 'off' in experiment:
    #     return opt_off
    # else:
    #     return ''
    return ''
    
def get_dataset(experiment):
    if 'stump' in experiment:
        return stump
    elif 'lego' in experiment:
        return lego
    else:
        return ''
    
def get_title(experiment):
    if 'LPIPS' in experiment:
        text = get_text(experiment).replace('LPIPS', 'LPIPS$\\downarrow$')
    if 'SSIM' in experiment:
        text = get_text(experiment).replace('LPIPS', 'SSIM$\\uparrow$')
    elif 'PSNR' in experiment:
        text = get_text(experiment).replace('LPIPS', 'PSNR$\\uparrow$')

    return text + get_model(experiment) + get_opt(experiment) + get_dataset(experiment)

import re

def get_number(experiment):
    return re.search(r'[^ -]*$', experiment).group(0)

def get_caption(experiment):
    text = 'Mean results achieved in the PSNR $\\uparrow$, SSIM $\\uparrow$ and LPIPS $\\downarrow$ metrics, with the relative change compared to the benchmark setting. Stump dataset is used. Lighting degradations. Nerfacto model is used. Camera optimizer is enabled.'
    types_clustered = {'Lightning'   : ['gamma', 'saturation'],
                   'Reductions'  : ['every', 'range'],
                   'Color noise' : ['blue-noise', 'green-noise', 'red-noise', 'noise-std'],
                   'Camera noise': ['pos-orient', 'position', 'orientation']}
    if 'lego' in experiment:
        text = text.replace('Stump', 'Lego')
    if 'ngp' in experiment:
        text = text.replace('Nerfacto', 'Instant-NGP')
    if 'off' in experiment:
        text = text.replace('enabled', 'disabled')
    for type_key, substrings in types_clustered.items():
        if any(substring in experiment for substring in substrings):        
            text = text.replace('Lighting', type_key)
    return text

        

def get_table_name(experiment):
    if 'every' in experiment:
        return 'Reduced Image Set'
    elif 'gamma' in experiment:
        return  'Gamma Correction'
    elif 'noise-std' in experiment:
        return 'Image Noise'
    elif 'pos' in experiment and 'orient' in experiment:
        return 'Combined Noise'
    elif 'pos' in experiment:
        return 'Positional Noise'
    elif 'orient' in experiment:
        return 'Orientation Noise'
    elif 'green' in experiment:
        return 'PnS Green Channel'
    elif 'red' in experiment:
        return 'PnS Red Channel'
    elif 'blue' in experiment:
        return 'PnS Blue Channel'
    elif 'satur' in experiment:
        return 'Saturation Change'
    elif 'range' in experiment:
        return 'Height Reduction'
    elif 'benchmark' in experiment:
        return 'Benchmark'
    else:
        return ''    