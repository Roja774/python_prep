section={
       "Students":{
                 "Roja":{
                       "Subject":{"Mathematics":75,"Physics":80,"Chemistry":89}
                      },
                "Aunsha":{
                        "Subject":{"Mathematics":80,"Physics":75,"Chemistry":90}
                       },

               "Surendra":{
                        "Subject":{"Mathematics":70,"Physics":69,"Chemistry":88}
                       }
 
                }
         }
print(section)
print(type(section))
print(section["Students"]["Roja"])
print(section["Students"]["Roja"]["Subject"])
print(section["Students"]["Roja"]["Subject"]["Physics"])
section["Students"]["Roja"]["Subject"]["Mathematics"]=90     #update mathematics marks 90
print("display update marks ")
print(section["Students"]["Roja"]["Subject"]["Mathematics"])
print(section)
section.update({"Students":{"Roja":{"Subject":{"Chemistry":99}}}})     # by using update() method to  update chemistry marks 
print("display update marks ")
print(section["Students"]["Roja"]["Subject"]["Chemistry"])
print(section)
for i in section.keys(): 
   
      print(section[i].keys())
ytt