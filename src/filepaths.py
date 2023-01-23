import os
import numpy as np

from pathlib import Path
from src.fileIO import load_json
from src.GUI import prompt_for_path


def get_directory_paths(root_path):
    '''
    Get target data path and results path from info dictionary file.
    Args:
        root_path: <string> path to root directory
    Returns:
        data_path: <string> path to data directory
        bg_path: <string> path to background directory
        results_path: <string> path to results directory
        info: <dict> information dictionary (info.json)
    '''
    directory_path = prompt_for_path(
        default=root_path,
        title='Select Target Directory',
        dir_path=True)
    return directory_path


def extractfile(directory_path,
                file_string):
    '''
    Pull file from directory path.
    Args:
        directory_path: <string> path to file
        file_string: <string> string contained within file name
    Returns:
        array: <array> array of selected files
    '''
    directory_list = sorted(os.listdir(directory_path))
    return [file for file in directory_list if file_string in file]


def get_files_paths(directory_path,
                    file_string):
    '''
    Get target files and directory paths depending on the operating system.
    Args:
        directory_path: <string> path to data directory
        file_string: <string> file extension (e.g. .csv)
    Returns:
        file_paths: <string> path to files
    '''
    data_files = extractfile(
        directory_path=directory_path,
        file_string=file_string)
    roi_file = prompt_for_path(
        default=directory_path,
        title='Select ROI File',
        file_path=True,
        file_type=[(f'{file_string}', f'*{file_string}')])
    return roi_file[0], data_files


def check_dir_exists(dir_path):
    '''
    Check to see if a directory path exists, and if not create one
    Args:
        dir_path: <string> directory path
    '''
    if os.path.isdir(dir_path) is False:
        os.mkdir(dir_path)


def results_directory(directory_path):
    '''
    Create results directory if one does not exist.
    Args:
        directory_path: <string> path to data directory
    Returns:
        results_path: <string> path to results directory
    '''
    results_path = Path(f'{directory_path}/Python_Results')
    check_dir_exists(dir_path=results_path)
    return results_path


def get_filename(file_path):
    '''
    Splits file path to remove directory path and file extensions.
    Args:
        file_path: <string> path to file
    Returns:
        file_name: <string> file name without path or extensions
    '''
    return os.path.splitext(os.path.basename(file_path))[0]


def ND_calculator(ND_string):
    '''
    Calculate transmission coefficient based on ND filter magnitude. Will return
    0ND if none present in string.
    Args:
        ND_string: <string> string containing ND filter string
    Returns:
        transmission: <float> transmission percentage as decimal (25% = 0.25)
    '''
    NDdict = {
        "0ND": 0.0,
        "01ND": 0.1,
        "02ND": 0.2,
        "03ND": 0.3,
        "04ND": 0.4,
        "05ND": 0.5,
        "06ND": 0.6,
        "07ND": 0.7,
        "08ND": 0.8,
        "09ND": 0.9,
        "10ND": 1.0}
    string_split = ND_string.split('_')
    ND = [string for string in string_split if 'ND' in string]
    if len(ND) == 0:
        ND_filter = '0ND'
    else:
        ND_filter = ND[0]
    transmission = (10 ** (-(NDdict[f'{ND_filter}'])))
    return transmission


def get_integration_time(integration_string):
    '''
    Get integration time from string. Returns 1s without integration string.
    Can cope with int100, or 100ms integration string formats.
    Args:
        integration_string: <string> string containing integration time
    Returns:
        integration_time: <float> integration time in s
    '''
    string_split = integration_string.split('_')
    int_time_string = [string for string in string_split if 'int' in string]
    ms_time_string = [string for string in string_split if 'ms' in string]
    time_string = np.append(int_time_string, ms_time_string)
    if len(time_string) == 0:
        integration_time = 1000.00
    else:
        integration_time = (float([
            time[3:] if 'int' in time
            else time[: -2]
            for time in time_string][0])) / 1000
    return integration_time


def get_wavelength(wavelength_string):
    '''
    Get wavelength information from string, string must contain "nm" somewhere.
    Args:
        wavelength_string: <string> string containing some number with nm
    Returns:
        wavelength: <string> wavelength number in nm
    '''
    string_split = wavelength_string.split('_')
    wav_string = [string for string in string_split if 'nm' in string]
    if len(wav_string) == 0:
        wavelength_string = '0nm'
        wavelength_digits = [s for s in wavelength_string if s.isdigit()]
        wavelength = float(('').join(wavelength_digits))
    else:
        wavelength_string = wav_string[0]
        wavelength_digits = [s for s in wavelength_string if s.isdigit()]
        wavelength = float(('').join(wavelength_digits))
    return wavelength


def roi_sample_information(file_path):
    '''
    Pull sample parameters from file name string for region of interest file.
    Args:
        file_path: <string> path to file
    Returns:
        sample_parameters: <dict>
    '''
    file_name = get_filename(file_path=file_path)
    file_split = file_name.split('_')
    transmission = ND_calculator(ND_string=file_name)
    integration = get_integration_time(integration_string=file_name)
    wavelength = get_wavelength(wavelength_string=file_name)
    return {
        'File Name': file_name,
        'File Path': f'{file_path}',
        'Primary String': file_split[0],
        'Secondary String': file_split[1],
        'Transmission': transmission,
        'Integration Time': integration,
        'Wavelength': wavelength}
