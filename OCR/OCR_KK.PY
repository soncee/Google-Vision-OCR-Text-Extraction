import cv2
import numpy as np
from PIL import Image as PILImage
from flask import Flask, request, jsonify
import cv2
import numpy as np
from google.cloud import vision_v1
import os
import re
import io




os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '#'

app = Flask(__name__)
@app.route('/extract_text', methods=['POST'])
def extract_text_from_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    image_temp = 'temp_image.jpg'
    file.save(image_temp) 

    contours,thresh,img_resize,img = image_processing(image_temp)

    def cropAtas(img):
        box = []
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            if (100<w<1200 and h<150 and y<1000 and x>10):
                image = cv2.rectangle(img_resize,(x,y),(x+w,y+h),(0,255,0),1)
                box.append([x,y,w,h])
        mask = np.zeros_like(image)
        for b in box:
            x, y, w, h = b
            mask[y:y+h, x:x+w] = image[y:y+h, x:x+w]
        return mask

    def cropBawah(img):
        box = []
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            if (100<w<1200 and h<120 and y>1250 and x>10):
                image = cv2.rectangle(img_resize,(x,y),(x+w,y+h),(0,255,0),1)
                box.append([x,y,w,h])
        mask = np.zeros_like(image)
        for b in box:
            x, y, w, h = b
            mask[y:y+h, x:x+w] = image[y:y+h, x:x+w]
        return mask
    
    def cropBawah(img):
        box = []
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            if (100<w<1200 and h<120 and y>1250 and x>10):
                image = cv2.rectangle(img_resize,(x,y),(x+w,y+h),(0,255,0),1)
                box.append([x,y,w,h])
        mask = np.zeros_like(image)
        for b in box:
            x, y, w, h = b
            mask[y:y+h, x:x+w] = image[y:y+h, x:x+w]
        return mask
    def cropNama(img):
        box = []
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            if (550<w<1000 and h<105 and y<1000 and x<300):
                image = cv2.rectangle(img_resize,(x,y),(x+w,y+h),(0,255,0),1)
                box.append([x,y,w,h])
        mask = np.zeros_like(image)
        for b in box:
            x, y, w, h = b
            mask[y:y+h, x:x+w] = image[y:y+h, x:x+w]
        return mask
    
    def cropNik(img):
        box = []
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            if (280<w<360 and h<95 and x<1500 and y<1000):
                image = cv2.rectangle(img_resize,(x,y),(x+w,y+h),(0,255,0),1)
                box.append([x,y,w,h])
        mask = np.zeros_like(image)
        for b in box:
            x, y, w, h = b
            mask[y:y+h, x:x+w] = image[y:y+h, x:x+w]
        return mask
    
    def cropGender(img):
        box = []
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            if (100<w<250 and h<95 and x<1500 and y<1000):
                image = cv2.rectangle(img_resize,(x,y),(x+w,y+h),(0,255,0),1)
                box.append([x,y,w,h])
        mask = np.zeros_like(image)
        for b in box:
            x, y, w, h = b
            mask[y:y+h, x:x+w] = image[y:y+h, x:x+w]
        return mask
    
    def cropPendidikan(img):
        box = []
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            if (450<w<600 and h<500 and 2000<x<2400 and y<1500):
                image = cv2.rectangle(img_resize,(x,y),(x+w,y+h),(0,255,0),1)
                box.append([x,y,w,h])
        mask = np.zeros_like(image)
        for b in box:
            x, y, w, h = b
            mask[y:y+h, x:x+w] = image[y:y+h, x:x+w]
        return mask
    
    def cropPekerjaan(img):
        box = []
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            if (450<w<600 and h<500 and x>2500 and y<1500):
                image = cv2.rectangle(img_resize,(x,y),(x+w,y+h),(0,255,0),1)
                box.append([x,y,w,h])
        mask = np.zeros_like(image)
        for b in box:
            x, y, w, h = b
            mask[y:y+h, x:x+w] = image[y:y+h, x:x+w]
        return mask
    
    def cropAyah(img):
        box = []
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            if (300<w<1200 and h<150 and y>1250 and 1500<x<2100):
                image = cv2.rectangle(img_resize,(x,y),(x+w,y+h),(0,255,0),1)
                box.append([x,y,w,h])
        mask = np.zeros_like(image)
        for b in box:
            x, y, w, h = b
            mask[y:y+h, x:x+w] = image[y:y+h, x:x+w]
        return mask
    
    def cropIbu(img):
        box = []
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            if (300<w<1200 and h<150 and y>1250 and x>2100):
                image = cv2.rectangle(img_resize,(x,y),(x+w,y+h),(0,255,0),1)
                box.append([x,y,w,h])
        mask = np.zeros_like(image)
        for b in box:
            x, y, w, h = b
            mask[y:y+h, x:x+w] = image[y:y+h, x:x+w]
        return mask
    
    atas = cropAtas(img)
    cv2.imwrite('atas.jpg',atas)
    cv2.imwrite('dob.jpg',atas)
    cv2.imwrite('agama.jpg',atas)
    bawah = cropBawah(img)
    cv2.imwrite('bawah.jpg',bawah)
    nama = cropNama(img)
    cv2.imwrite("nama.jpg", nama)
    nik = cropNik(img)
    cv2.imwrite("nik.jpg", nik)
    gender = cropGender(img)
    cv2.imwrite("gender.jpg", gender)
    pendidikan = cropPendidikan(img)
    cv2.imwrite('pendidikan.jpg',pendidikan)
    pekerjaan = cropPekerjaan(img)
    cv2.imwrite('pekerjaan.jpg',pekerjaan)
    ibu = cropIbu(img)
    cv2.imwrite('ibu.jpg',ibu)
    ayah = cropAyah(img)
    cv2.imwrite('ayah.jpg',ayah)
    cv2.imwrite('wni.jpg',bawah)
    cv2.imwrite('perkawinan.jpg',bawah)
    cv2.imwrite('hub.jpg',bawah)


    image_path_nama = 'nama.jpg'


    image_path_nik = 'nik.jpg'

    image_path_gender = 'gender.jpg'

    image_path_tempat = 'atas.jpg'

    image_path_dob = 'dob.jpg'

    image_path_agama = 'agama.jpg'

    image_path_pendidikan = 'pendidikan.jpg'

    image_path_pekerjaan = 'pekerjaan.jpg'

    image_path_perkawinan = 'perkawinan.jpg'

    image_path_warganegara = 'wni.jpg'

    image_path_ayah = 'ayah.jpg'

    image_path_ibu = 'ibu.jpg'
    
    # Perform text extraction using Google Cloud Vision API
    result_nama = extract_text(image_path_nama)
    result_nik = extract_text(image_path_nik)
    result_gender = extract_text(image_path_gender)
    result_tempat = extract_text(image_path_tempat)
    result_dob = extract_text(image_path_dob)
    result_agama = extract_text(image_path_agama)
    result_pendidikan = extract_text(image_path_pendidikan)
    result_pekerjaan = extract_text(image_path_pekerjaan)
    result_perkawinan = extract_text(image_path_perkawinan)
    result_warganegara = extract_text(image_path_warganegara)
    result_ayah = extract_text(image_path_ayah)
    result_ibu = extract_text(image_path_ibu)


    os.remove(image_temp)

    # Return the extracted results as JSON
    return jsonify(result_nama,result_nik,result_gender,result_tempat,result_dob,result_agama,result_pendidikan,result_pekerjaan,result_perkawinan,result_warganegara,result_ayah,result_ibu) 

def image_processing(image_path):

    img = cv2.imread(image_path,0)
    new_size = (3508,2480)
    img_resize = cv2.resize(img,new_size)
    img_resize = cv2.resize(img,new_size)
    thresh,img_bin = cv2.threshold(img_resize,128,255,cv2.THRESH_BINARY |cv2.THRESH_OTSU)
    img_bin = 255-img_bin
    cv2.imwrite('Detected_Image.jpg',img_bin)
    kernel_len = np.array(img_resize).shape[1]//100
    ver_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_len))
    hor_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_len, 1))
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    image_1 = cv2.erode(img_bin, ver_kernel, iterations=3)
    vertical_lines = cv2.dilate(image_1, ver_kernel, iterations=3)
    cv2.imwrite("Detected_Image.jpg",vertical_lines)
    image_2 = cv2.erode(img_bin, hor_kernel, iterations=3)
    horizontal_lines = cv2.dilate(image_2, hor_kernel, iterations=3)
    cv2.imwrite("Detected_Image.jpg",horizontal_lines)
    img_vh = cv2.addWeighted(vertical_lines, 1, horizontal_lines, 1, 0.0)
    img_vh = cv2.erode(~img_vh, kernel, iterations=2)
    thresh, img_vh = cv2.threshold(img_vh,128,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    contours, _ = cv2.findContours(img_vh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours,thresh,img_resize,img


def extract_text(image_path):
    # Instantiate a client
    client = vision_v1.ImageAnnotatorClient()

    # Read the image file into memory
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    # Create an image instance
    image = vision_v1.Image(content=content)
    

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
        if "nama" in image_path.lower():
            names = extract_names(extracted_text)
            return {"nama": names}
        elif "nik" in image_path.lower():
            nik=extract_nik(extracted_text)
            return {"nik": nik}
        elif "gender" in image_path.lower():
            gender=extract_gender(extracted_text)
            return {"gender": gender}
        elif "atas" in image_path.lower():
            tempat=extract_tempat_lahir(extracted_text)
            return {"tempat lahir": tempat}
        elif "dob" in image_path.lower():
            dob = extract_dob(extracted_text)
            return {"tanggal lahir": dob}
        elif "agama" in image_path.lower():
            agama = extract_agama(extracted_text)
            return {"agama": agama}
        elif "pendidikan" in image_path.lower():
            pendidikan = extract_pendidikan(extracted_text)
            return {"pendidikan": pendidikan}
        elif "pekerjaan" in image_path.lower():
            pekerjaan = extract_pekerjaan(extracted_text)
            return {"pekerjaan": pekerjaan}
        elif "perkawinan" in image_path.lower():
            perkawinan = extract_perkawinan(extracted_text)
            return {"status perkawinan": perkawinan}
        elif "wni" in image_path.lower():
            warganegara = extract_kewarganegaraan(extracted_text)
            return {"kewarganegaraan": warganegara}
        elif "hub" in image_path.lower():
            hub = extract_hubungan(extracted_text)
            return {"status hubungan": hub}
        elif "ayah" in image_path.lower():
            ayah = extract_ayah(extracted_text)
            return {"ayah ": ayah}
        elif "ibu" in image_path.lower():
            ibu = extract_ibu(extracted_text)
            return {"ibu ": ibu}
        
    return None

def extract_names(text):
    names = re.findall(r'[A-Z ]+(?=\n|$)', text, re.IGNORECASE)
    names = [name for name in names if name.upper() != "NAMA LENGKAP"]
    return names
def extract_nik(text):
    pattern = r'\d{16}'
    match = re.findall(pattern,text)
    if match:
        return match
    else:
        return None
    
def extract_gender(text):
    pattern = r'\b(LAKI-LAKI|PEREMPUAN|LAKHLAKI)\b'
    match = re.findall(pattern,text)
    if match:
        return match
    else:
        return None
def extract_tempat_lahir(text):
    pattern = r'\d{16}\s(?:LAKHLAKI|PEREMPUAN|LAKI-LAKI|LAKILAKI|LAKI LAKI)\s(.+)'
    matches = re.findall(pattern, text)
    if matches:
        return matches
    else:
        return None
def extract_dob(text):
    pattern = r'\d{2}-\d{2}-\d{4}'
    match = re.findall(pattern,text)
    if match:
        return match
    else:
        return None
    
def extract_agama(text):
    pattern = r'\d{2}-\d{2}-\d{4}\s(.+)'
    match = re.findall(pattern,text)
    if match:
        return match
    else:
        return None

def extract_pendidikan(text):
    pattern = r'(?:(?<!\S)Pendidikan(?!\S).*)'
    lines = text.split('\n')
    filtered_lines = [line for line in lines if not re.search(pattern, line, re.IGNORECASE)]
    return filtered_lines

def extract_pekerjaan(text):
    names = re.findall(r'[A-Z ]+(?=\n|$)', text, re.IGNORECASE)
    names = [name for name in names if name.upper() != "JENIS PEKERJAAN"]
    return names

def extract_kewarganegaraan(text):
    pattern = r'\b(WNI|WNA|INDONESIA|WINI)\b'
    match = re.findall(pattern,text)
    if match:
        return match
    else:
        return None

def extract_perkawinan(text):
    pattern = r'\b(BELUM KAWIN|KAWIN)\b'
    match = re.findall(pattern,text)
    if match:
        return match
    else:
        return None

def extract_hubungan(text):
    pattern = r'\b(ISTRI|AYAH|IBU|SUAMI|ANAK|KEPALA KELUARGA)\b'
    match = re.findall(pattern,text,re.IGNORECASE)
    if match:
        return match
    else:
        return None

def extract_ayah(text):
    names = re.findall(r'[A-Z ]+(?=\n|$.)', text,re.IGNORECASE)
    names = [name for name in names if name.upper() != "AYAH"]
    return names

def extract_ibu(text):
    names = re.findall(r'[A-Z ]+(?=\n|$)', text,re.IGNORECASE)
    names = [name for name in names if name.upper() != "IBU"]
    return names






if __name__ == '__main__':
    app.run(debug=True)


