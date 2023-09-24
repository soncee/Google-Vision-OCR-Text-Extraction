import os
import io
from google.cloud import vision
from google.cloud.vision_v1 import types 
from google.cloud import vision_v1
from typing import Sequence
import re
from flask import Flask, request, jsonify

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'#'

client = vision.ImageAnnotatorClient()

app = Flask(__name__)

@app.route('/extract-id-card-info', methods=['POST'])
def extract_id_card_info():
    # Get the image URI from the request body
    image_uri = request.json['image_uri']

    # Call the function to extract ID card information
    result = extract_id_card_info(image_uri)

    if result:
        return jsonify(result)
    else:
        return jsonify({'error': 'No text found in the image.'})
    
def extract_id_card_info(image_uri):


    # Instantiate a client
    client = vision_v1.ImageAnnotatorClient()


    # Create an image instance
    image = vision.Image()
    image.source.image_uri = image_uri

    # Specify the feature to detect text
    feature = vision_v1.Feature(
        type_=vision_v1.Feature.Type.DOCUMENT_TEXT_DETECTION
    )

    # Create the request
    request = vision_v1.AnnotateImageRequest(
        image=image,
        features=[feature]
    )

    # Send the request to the API
    response = client.annotate_image(request)

    # Process the response
    text_annotations = response.text_annotations
    if text_annotations:
        extracted_text = text_annotations[0].description
        extracted_text = extracted_text.replace(':', '')
        extracted_text = extracted_text.replace('=', '')

        # Extract specific fields based on your ID card structure
        # Example:
        name = extract_name(extracted_text)
        nik = extract_nik(extracted_text)
        address = extract_address(extracted_text)
        dob = extract_date_of_birth(extracted_text)
        status_perkawinan = extract_status_perkawinan(extracted_text)
        rt_rw = extract_rt_rw(extracted_text)
        kecamatan = extract_kecamatan(extracted_text)
        kelurahan = extract_kelurahan(extracted_text)
        provinsi = extract_provinsi(extracted_text)
        gender = extract_gender(extracted_text)
        agama = extract_agama(extracted_text)
        kerja = extract_pekerjaan(extracted_text)

        # Return the extracted information
        result ={
            'name': name,
            'nik': nik,
            'address': address,
            'tempat tanggal lahir': dob,
            'marital stat': status_perkawinan,
            'rt/rw': rt_rw,
            'kel/des': kelurahan,
            'kecamatan': kecamatan,
            'provinsi' : provinsi,
            'gender' : gender,
            'agama' : agama,
            'pekerjaan' : kerja
        }
        return result
    else:
        return None


def extract_name(text):
  
    lines = text.split('\n')
    for i, line in enumerate(lines):
        match = re.search(r'\s*(.*?) \d{2}-\d{2}-\d{4}',line)
        if match:
            if i+1<len(lines):
                return lines[i-1].strip()
    return None

def extract_nik(text):

    pattern = r'\d{16}'
    match = re.search(pattern,text)
    if match:
        return match.group()
    else:
        return None



def extract_address(text):

    lines = text.split('\n')
    for i, line in enumerate(lines):
        match = re.search(r'\b(\d{3}|0\d{2})\s*[/7]\s*(\d{3}|0\d{2})\b',line)
        if match:
            if i+1<len(lines):
                return lines[i-1].strip()
    return None

def extract_date_of_birth(text):

    pattern = r'(.*?) \d{2}-\d{2}-\d{4}'
    match = re.search(pattern, text)
    if match:
        return match.group()
    else:
        return None

def extract_status_perkawinan(text):
    # Implement your logic to extract the name from the text
    # Example:
    # Search for the line containing 'NAMA' and extract the name from the following line
    pattern = r'\b(belum kawin|kawin|cerai hidup|cerai mati|married|not married)\b'
    match = re.search(pattern, text,re.IGNORECASE)
    if match:
        return match.group(1)
    else:
        return None
    

def extract_rt_rw(text):
    pattern = r'\b(\d{3}|0\d{2})\s*[/7]\s*(\d{3}|0\d{2})\b'
    match = re.search(pattern,text)
    if match:
        return match.group()
    else:
        return None
    
def extract_kecamatan(text):
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        match = re.search(r'\b(\d{3}|0\d{2})\s*[/7]\s*(\d{3}|0\d{2})\b',line)
        if match:
            if i+1<len(lines):
                return lines[i+2].strip()
    return None

def extract_kelurahan(text):
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        match = re.search(r'\b(\d{3}|0\d{2})\s*[/7]\s*(\d{3}|0\d{2})\b',line)
        if match:
            if i+1<len(lines):
                return lines[i+1].strip()
    return None

def extract_provinsi(text):
    
    pattern = r'PROVINSI\s(.+)'
    match = re.search(pattern,text)
    if match:
        return match.group()
    else:
        return None
    
def extract_gender(text):
    pattern = r'(laki-laki|perempuan)'
    match = re.search(pattern,text,re.IGNORECASE)
    if match:
        return match.group()
    else:
        return None
    
def extract_agama(text):
    pattern = r'(kristen|islam|buddha|katholik|Hindu|konghuchu|CHRISTIAN|MUSLIM)'
    match = re.search(pattern,text,re.IGNORECASE)
    if match:
        return match.group()
    else:
        return None
# Usage example

def extract_pekerjaan(text):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        match = re.search(r'(WNI|RUSIA)',line)
        if match:
            if i+1<len(lines):
                return lines[i-1].strip()
    return None


if __name__ == '__main__':
    app.run(debug=True)