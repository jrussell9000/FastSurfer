from yacs.config import CfgNode as CN

_C = CN()

# ---------------------------------------------------------------------------- #
# HDF5 options
# ---------------------------------------------------------------------------- #
_C.HDF5 = CN()

# name of hdf5-dataset (default: testsuite_2.hdf5)
_C.HDF5.FILE_PREFIX_NAME = "testsuite_2.hdf5"

# path of hdf5-dataset (default: data)
_C.HDF5.PATH = "data"

# ---------------------------------------------------------------------------- #

# Which plane to put into file (coronal (default), axial or sagittal)
_C.PLANES = ["axial", "coronal", "sagittal"]

# size of the 3D patch size
# to crop from input image'
_C.PATCH_SIZE = (128, 128, 128)

# Directory with images to load
_C.DATA_DIR = ""


# Number of splits in cross validation
_C.NUM_SPLITS = 1


# To read and apply warp fields to images and store warped images
_C.LOAD_AUXILIARY_DATA = False

# map between moving and fixed subject ids in registered dataset
_C.REG_DATA_CSV = "subids_labeled2unlabeled.csv"

# Directory with registered data as auxiliary dataset
_C.REG_DATA_DIR = ""

# name of warp field
# _C.WARP_FIELD_FILENAME = "1Warp.nii.gz"

# to compute and store talairach coordinates
_C.STORE_TALAIRACH = False

# Number of pre- and succeeding slices (default: 3)
_C.THICKNESS = 3

_C.EDGE_WEIGHING = True

# Csv-file listing subjects to include in file, training
_C.TRAIN_CSV_FILE_PATH = "train_split.csv"

# Csv-file listing subjects to include in file validation
_C.VAL_CSV_FILE_PATH = "val_split.csv"

# Default name of original images. FreeSurfer orig.mgz is default (mri/orig.mgz)
# or native_t1.nii for image in native space
_C.IMAGE_NAME = "mri/orig/001.mgz"

# Name of the cerebellum sub-segmentation file,
# SUIT labels: suit_fs_merged_cleaned.mgz
# Manual labels: cleaned_manual_fs_bs_corr.mgz
_C.CEREB_SUBSEG_NAME = "suit_fs_merged_cleaned.mgz.mgz"

# whether the subseg label are manually annotated or generated by SUIT
_C.MANUAL_SUBSEG = False

# the direction of primary slice,
# the plane (axial, coronal, sagittal) that the last dimension of
# 3D volume corresponds to
_C.PRIMARY_SLICE_DIR = "axial"


# The name of warped cropped auxiliary  t1 image
_C.AUXILIARY_IMAGE = "T1_warped_cropped.nii.gz"

# The name of warped cropped auxiliary  label image
_C.AUXILIARY_LABEL = "label_warped_cropped.nii.gz"


def get_cfg_dataset():
    """Get a yacs CfgNode object with default values for my_project."""
    # Return a clone so that the defaults will not be altered
    # This is for the "local variable" use pattern
    return _C.clone()