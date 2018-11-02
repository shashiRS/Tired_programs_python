# coding: utf8
from googleplaces import GooglePlaces, types, lang
import imgkit
import schedule
import conf
from conf import db,app
import logging
import base64
import webbrowser
from flask import Flask,render_template,request
import time
from threading import Thread
import threading
import pdb
import re
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
class Builder(db.Model):
    __tablename__ = 'builders'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    website=db.Column(db.String(500))
    local_number=db.Column(db.String(100))
    url=db.Column(db.String(500))
    lat=db.Column(db.String(500))
    lng=db.Column(db.String(500))
    address=db.Column(db.String(500))
    domain=db.Column(db.String(100))

    # city=db.Column(db.String(500))

db.create_all()
@app.route('/')
def index():
    t = Thread(name="mapThread")
    # print threading.current_thread() 
    print threading.currentThread()
    t.start()
    return render_template('googleindex.html')

@app.route('/search',methods=['GET','POST'])
def search():
   
    projectpath = request.form['projectFilepath']
    logging.debug(projectpath)
    YOUR_API_KEY = 'AIzaSyBirb_Js--NuPNkGBeKgijDPKxKbLTYCiM'
    # "OVER_QUERY_LIMIT" indicates that you are over your quota.
    google_places = GooglePlaces(YOUR_API_KEY)
    term=projectpath
    # imgkit.from_url('https://www.google.com/maps/search/matri+mall/@12.9918927,77.5685398,17z/data=!3m1!4b1', 'mantri.jpg')
   
    # print google_places
    # You may prefer to use the text_search API, instead.
    # pdb.set_trace()
    query_result = google_places.nearby_search(location='%s, %s' % (12.9330, 77.7368), keyword=term,radius=2000)
 
       
    # If types param contains only 1 item the request to Google Places API
    # will be send as type param to fullfil:
    # http://googlegeodevelopers.blogspot.com.au/2016/02/changes-and-quality-improvements-in_16.html

    # if query_result.has_attributions:
    #     print query_result.html_attributions
    # print query_result.places
    for place in query_result.places:
        # Returned places from_url a query are place summaries.
        logging.debug(place.name)  
        # logging.debug(place.geo_location['lat'])
        # logging.debug(place.geo_location['lng'])
        logging.debug(place.place_id)
        logging.debug(place.get_details())
        logging.debug(place.local_phone_number)
        logging.debug(place.international_phone_number)
        logging.debug(place.url)

        # The following method has to make a further API call.
        # logging.debug(place.get_details())
        # Referencing any of the attributes below, prior to making a call to
        # get_details() will raise a googleplaces.GooglePlacesAttributeError.
        # print place.details # A dict matching the JSON response from Google.
            
                
        #encode and decode the string
        place_name_encode=base64.encodestring(place.name)
        place_name=base64.b64decode(place_name_encode)
        logging.debug(place_name)
            
        place_url_encode=base64.encodestring(place.url)
        place_url=base64.b64decode(place_url_encode)
        logging.debug(place_url)

        if place.local_phone_number==None:
            phone_number='None'
        else:
            phone_number_encode=base64.encodestring(place.local_phone_number)
            phone_number=base64.b64decode(phone_number_encode)
        # logging.debug(place.details)
          
           
        dmain=[]
        # regex = re.compile(place_name, re.IGNORECASE)

        # match = regex.search(term)  # From your file reading code.
        # if match is not None:
        
        dommm=''
        domm=''
        fetch_data = db.session.query(Builder).all()
        dommm=place_url.split('/')[2]
                                        
        if 'www' in dommm:
            dmain.append(dommm.split('www.',1)[1])
            domn=dommm.split('www.',1)[1]

        else:
            dmain.append(dommm)
            domn=domm
        if fetch_data==[]:
            #database dont have an entry
            new=Builder(name=place_name,website=place.website,local_number=phone_number,url=place_url,lat=place.geo_location['lat'],lng=place.geo_location['lng'],address=place.vicinity,domain=domn)
            db.session.add(new)
            db.session.commit()
        elif Builder.query.filter(Builder.url == place_url).count()>=1:
            pass
                #already present in database
        else:
            new=Builder(name=place_name,website=place.website,local_number=phone_number,url=place_url,lat=place.geo_location['lat'],lng=place.geo_location['lng'],address=place.vicinity,domain=domn)
            db.session.add(new)
            db.session.commit()
               
            # buffer = BytesIO(urllib.urlopen(urll).read())
            # image = Image.open(buffer)
            # image.save(count+".png")
        # else:
        #     print(place_name)   


    fetch_data = db.session.query(Builder).all()
    data_list=[{'id':data.id,'name':data.name,'website':data.website,'number':data.local_number,'url':data.url,'lat':data.lat,'lng':data.lng,'address':data.address,'domain':data.domain} for data in fetch_data]
    return render_template('google_place_detail.html',data=data_list)
# schedule.every(5).minutes.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

if __name__ == '__main__':
    app.run(host='localhost')
    # webbrowser.open_new_tab('http://127.0.0.1:5000/')
    # Adding and deleting a place
# try:
#     added_place = google_places.add_place(name='Mom and Pop local store',
#             lat_lng={'lat': 51.501984, 'lng': -0.141792},
#             accuracy=100,
#             types=types.TYPE_HOME_GOODS_STORE,
#             language=lang.ENGLISH_GREAT_BRITAIN)
#     print added_place.place_id # The Google Places identifier - Important!
#     print added_place.id

#     # Delete the place that you've just added.
#     google_places.delete_place(added_place.place_id)
# except GooglePlacesError as error_detail:
#     # You've passed in parameter values that the Places API doesn't like..
#     print error_detail