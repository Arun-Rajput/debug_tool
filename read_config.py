# read config file
# configuration parser

import sys
from os import path
from configparser import ConfigParser

file_path = "C:\\Users\\arurajpu\\Desktop\\Debug tools"

def read_config(file_name, section, option):
          ''' read the config file , you need to pass the filename and section'''
          config_file = path.join(file_path, file_name)
          parser =  ConfigParser()
          parser.read(config_file)
          if parser.has_section(section):
                    if section == 'phone_type':
                              # it will return a list of options availabe in section 'phone_type'
                              return parser.get(section, option).split(",")
                    else:
                              return parser.get(section, option)
          else:
                    raise ValueError("Section %s doesnot exist in %s file" %(section, file_name))
          

if __name__== "__main__":
          # run the following test to check config praser is working or not
          config_op = read_config('tb_config.ini','phone_type', 'audio_only_phones')
          print ("Config output: %s" %(config_op))
          config_out = read_config('tb_config.ini', 'cucm', 'lhr_cucm_pub')
          print ('config out: %s' %(config_out))
          
          
          

