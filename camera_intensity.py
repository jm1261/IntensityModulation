import datetime
import src.fileIO as io
import src.filepaths as fp
import src.userinput as ui
import src.plotting as plot
import src.analysis as anal

from pathlib import Path
''' finish this, only suitable for windows interface currently'''


if __name__ == '__main__':

    ''' Date '''
    date = ('').join((f'{datetime.datetime.now().date()}'.split('-')))

    ''' Organisation '''
    root = Path().absolute()
    root = 'Z:\\Josh\\PhD_Project\\Slow_Light'
    directory_path = fp.get_directory_paths(root_path=root)
    roi_file, data_files = fp.get_files_paths(
        directory_path=directory_path,
        file_string='.bmp')
    results_path = fp.results_directory(directory_path=directory_path)

    ''' Process ROI File '''
    roi_parameters = fp.roi_sample_information(file_path=roi_file)
