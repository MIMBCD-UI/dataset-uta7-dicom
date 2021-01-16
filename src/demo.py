#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""demo.py: a small and simple demo for this dataset."""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "AGPLv3 & CC-BY-SA-4.0"
__version__     = "0.1.0"
__status__      = "Production"
__copyright__   = "Copyright 2021, Instituto Superior Técnico (IST)"
__credits__     = [
	"Hugo Lencastre",
	"Nádia Mourão",
	"Bruno Dias",
	"Luís Ribeiro Gomes",
	"Bruno Oliveira",
	"Carlos Santiago",
	"Jacinto C. Nascimento",
	"Pedro Miraldo",
	"Nuno Nunes"
]

import sys, os.path
import matplotlib.pyplot as plt
from pydicom import dcmread
from pydicom.data import get_testdata_file

pathDirname = os.path.dirname(__file__)
joinPath = os.path.join(pathDirname, '..', '..', '..')
pathAbsPath = os.path.abspath(joinPath)

repoJoinPath = os.path.join(pathAbsPath, 'Git', 'dataset-uta7-dicom')
sys.path.append(repoJoinPath)
repoAbsPath = os.path.abspath(repoJoinPath)

datasetJoinPath = os.path.join(repoAbsPath, 'dataset', 'Anonymized1')
sys.path.append(datasetJoinPath)
datasetAbsPath = os.path.abspath(datasetJoinPath)

fileNameToRead = "MG000000.dcm"
fullPathToFile = os.path.join(datasetJoinPath, fileNameToRead)

ds = dcmread(fullPathToFile)

# Normal mode:
print()
print(f"File path........: {fullPathToFile}")
print(f"SOP Class........: {ds.SOPClassUID} ({ds.SOPClassUID.name})")
print()

pat_name = ds.PatientName
display_name = pat_name.family_name + ", " + pat_name.given_name
print(f"Patient's Name...: {display_name}")
print(f"Patient ID.......: {ds.PatientID}")
print(f"Modality.........: {ds.Modality}")
print(f"Study Date.......: {ds.StudyDate}")
print(f"Image size.......: {ds.Rows} x {ds.Columns}")
print(f"Pixel Spacing....: {ds.PixelSpacing}")

# use .get() if not sure the item exists, and want a default value if missing
print(f"Slice location...: {ds.get('SliceLocation', '(missing)')}")

# plot the image using matplotlib
plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
plt.show()

# ==================== END File ==================== #