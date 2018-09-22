# A prediction API 

Train a model, based on date and various other parameters, and get predictions
on utilization.

# Check the full explanation video (GR)
[![Πρόβλεψη Τζίρου με Machine Learning #66, live](https://img.youtube.com/vi/mKeI0Je9cKs/0.jpg)](https://www.youtube.com/watch?v=mKeI0Je9cKs)

# Installation
Requirements
- You need to have [Docker](https://docs.docker.com/engine/installation/) installed

Run in root folder,
~~~~
cp .env.example .env
docker-compose build && docker-compose up -d
~~~~

Login to the container,
~~~~
docker exec -it ai /bin/bash -c "TERM=$TERM exec bash"
~~~~

To check it works,
~~~~
python predict.py 1
~~~~

You should see, something like,
~~~~
[[ 0  0  0  0  0  0  0  0 75 76 78 79 82 83 86 83 82 79 78 75 73  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0 66 68 69 71 73 75 77 75 73 70 68 65 64  0  0  0]]
~~~~

# By SocialNerds
* [SocialNerds.gr](https://www.socialnerds.gr/)
* [YouTube](https://www.youtube.com/SocialNerdsGR)
* [Facebook](https://www.facebook.com/SocialNerdsGR)
* [Twitter](https://twitter.com/socialnerdsgr)