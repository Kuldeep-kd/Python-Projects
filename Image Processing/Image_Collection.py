import cv2
import os
import urllib.request as rq

link = "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152"
neg_links = rq.urlopen(link).read().decode()

if not os.path.exists('negs'):
	os.makedirs('negs')

links = neg_links.split('\r\n')

i = 0
for x in links:
	try:
		if not os.path.isfile(f"negs/{i}.jpg"):
			rq.urlretrieve(x, f"negs/{i}.jpg")
			img = cv2.imread(f"negs/{i}.jpg")
			img = cv2.resize(img, (100,100))

			cv2.imwrite(f"negs/{i}.jpg", img)
			print(f"negs/{i}.jpg"+" Done\n")
			os.system('cls')
			print(f"{'█'*(int)(i*100/len(links))} {(i*100/len(links))}")
			i+=1
		else:
			i+=1
	except Exception as e:
		i+=1

cv2.waitKey(0)