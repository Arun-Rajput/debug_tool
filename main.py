import sys
import os
import argparse
from read_config import read_config

def main(file_name, section, option):
          # read the config file
          return read_config(file_name,section, option)

def argument():
          parser = argparse.ArgumentParse(description = "sum the integer at command line")



if __name__ == '__main__':
          tb_config = 'tb_config.ini'
          phone_configuration = 'phone_configuration.ini'
          config_out = main(phone_configuration, 'Satndard voicemail', 'Voicemail_profile_sea')
          print(config_out)
          config_out = main(phone_configuration, 'Satndard voicemail', 'No_answer_ring_duration')
          print(config_out)
