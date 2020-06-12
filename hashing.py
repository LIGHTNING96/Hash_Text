# hashing module Coded By Muhammed Mater 
# thanks to Mahmoud S. Al for edite the code
# facebook  : https://www.facebook.com/mody.saber.96343405 follow me
#!/usr/bin/python3

import os
import sys


banner = ("""
  _____  ___    _    _  _____          _   _ _____  ___    _   _  _  _   _  ___   
 (_   _)(  _ \ ( )  ( )(_   _)        ( ) ( )  _  )(  _ \ ( ) ( )(_)( ) ( )(  _ \ 
 /|| |  | (_(_) \ \/ / /|| |   ______ | |_| | (_) || (_(_)| |_| || ||  \| || ( (_)
(_)| |  |  _)_   )  ( (_)| |  (______)|  _  |  _  ) \__ \ |  _  || ||     || | __ 
   | |  | (_( ) / /\ \   | |          | | | | | | |( )_) || | | || || | \ || |(_ )
   ( )  (____/ ( )  (_)  ( )          (_) (_)_) (_) \(___)(_) (_)(_)(() (_)(____/ 
   /(          /(        /(                         (_)             (_)           
  (__)        (__)      (__)                                                      

[+]===== My Info =====[+]

Author    : Medo Mater
FaceBook  : https://www.facebook.com/xcberlin
WhatsApp  : +201066041330

"""   
)
import hashlib
class Fucken_hash:
  def fucken_hash(self,text,hash_type):
    text=text.encode("utf-8")
    hash_hash = hashlib.new(hash_type)
    hash_hash.update(text)
    return hash_hash.hexdigest()

print (banner)
