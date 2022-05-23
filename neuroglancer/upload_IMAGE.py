import argparse
import numpy as np
from cloudvolume import CloudVolume
import tifffile as tf
from joblib import Parallel


def create_image_layer(destination, shape):
	info = CloudVolume.create_new_info(
		num_channels 	= 1,
		layer_type	= 'image',
		data_type	= 'uint8',
		encoding	= 'raw',
		resolution	= [8,8,30],
		voxel_offset	= [0, 0, 0],
		chunk_size	= [64, 64, 16],
		volume_size	= shape
	)

	vol = CloudVolume(destination, compress=False, info=info, parallel=True)
	print(vol.info)
	vol.commit_info()
	return vol

# python upload.py **source** **destination**
# python upload.py ./test/ precomputed://file://test_output
def main():
	parser = argparse.ArgumentParser('Convert a folder of tif files to neuroglancer format')
	parser.add_argument('destination', help='Destination path for precomputed files, pre-pended with precomputed://file://, e.g. precomputed://file://**path** will write the files to ./**path**')
	args = parser.parse_args()

	raw_path = '/data12T/janechen/mitoEM/human_raw.tiff'
	im = tf.imread(raw_path)
	im = im.transpose((2, 1, 0))
	vol = create_image_layer(args.destination, im.shape)

	vol[:,:,:] = im

if __name__ == "__main__":
	main()
