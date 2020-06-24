from PIL import Image
import os
import imagehash
import csv

cutoff = 5
similarParent = []
imagesList = os.listdir('/Users/varshitrajput/Desktop/Images/')
for i in range(len(imagesList)):
    for j in range(i + 1, len(imagesList)):
        similar = []
        if imagesList[i].startswith('.') or imagesList[j].startswith('.'):
            break
        else:
            path1 = '/Users/varshitrajput/Desktop/Images/'+ str(imagesList[i])
            path2 = '/Users/varshitrajput/Desktop/Images/'+ str(imagesList[j])
            image1 = Image.open(path1)
            image2 = Image.open(path2)
            width1, height1 = image1.size
            width2, height2 = image2.size
            hash0 = imagehash.average_hash(image1) 
            hash1 = imagehash.average_hash(image2)
            if hash0 - hash1 < cutoff:
                similar.append(imagesList[i])
                similar.append(str(width1) + 'X' + str(height1))
                similar.append(imagesList[j])
                similar.append(str(width2) + 'X' + str(height2))
                similarParent.append(similar)
            else:
                continue


with open('Results.csv','w',newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(['IMAGE 1','RESOLUTION','IMAGE 2','RESOLUTION'])
    for i in similarParent:
        csvwriter.writerow(i)
print("\n\nProcess Completed")
print("Files Checked :",len(imagesList))
print("Output Saved in Results.csv")






