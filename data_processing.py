import matplotlib.pyplot as plt
import numpy as np
import nibabel as nib
import os

def load_and_save_imgs(filenr: int) -> np.ndarray:
    file_path = os.path.join('archive', 'BraTS2021_Training_Data', f'BraTS2021_{filenr:05d}')
    if filenr > 0.2*1667:
        save_path = os.path.join('gan_data','train_set')
    else:
        save_path = os.path.join('gan_data','test_set')

    data_t1_fn = os.path.join(file_path, f'BraTS2021_{filenr:05d}_t1.nii.gz')
    data_t1ce_fn = os.path.join(file_path, f'BraTS2021_{filenr:05d}_t1ce.nii.gz')

    if os.path.exists(data_t1_fn) and os.path.exists(data_t1ce_fn):

        data_t1 = get_raw_data(data_t1_fn)
        data_t1ce = get_raw_data(data_t1ce_fn)

        for i in range(data_t1.shape[2]):
            d_t1 = data_t1[:,:,i]
            d_t1ce = data_t1ce[:,:,i]
            if np.count_nonzero(d_t1ce) == 0:
                continue
            d = np.concatenate((d_t1, d_t1ce), axis=1)
            plt.imsave(os.path.join(save_path, f'BraTS2021_{filenr:05d}_{i:03d}.jpeg'), d, cmap='gray')

def get_raw_data(filename: str) -> np.ndarray:
    img = nib.load(filename)
    return img.get_fdata()

if __name__ == '__main__':
    if not os.path.exists(os.path.join('gan_data','train_set')):
        os.makedirs(os.path.join('gan_data','train_set'))

    if not os.path.exists(os.path.join('gan_data','test_set')):
        os.makedirs(os.path.join('gan_data','test_set'))

    for i in range(1667):
        load_and_save_imgs(i)
