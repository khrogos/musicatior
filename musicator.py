#!/usr/bin/env python 
# -*- coding:Utf-8 -*-

import os
import sys

###
# usage
# IN : nom du programme
# OUT: None
# DO : show how to usage the program
###
def usage(prog):
        print ("config file : ~/.musicatorrc")
        print ("shown available playlist : \n\t"+prog+" -show")
        print ("launch a playlist : \n\t"+prog+" -launch <playlist>")
        sys.exit(0);

###
# inList
# IN : playlist name, path to the playlists
# OUT: Boolean
# DO : check if the playlist is available
###
def inList(play, fold):
        found = False
        for playlist in os.listdir(fold):
                if(playlist == play):
                        found = True
                        break
        return found

###
# showPlaylist
# IN : path to the playlist
# OUT: None
# DO : shown the list of available playlist
###
def showPlaylist(fold):
        print ("available playlist : ")
        for playlist in os.listdir(fold):
                print ("\t- "+playlist)


###
# readConfigFile 
# IN : variable to search
# OUT: value to assign
# DO : search in the config file the values for
#      the playlist folder
###
def readConfigFile():

        config = open(os.getenv("HOME")+"/.musicatorrc", 'r')
        line = config.readline()
        result = None
        while(line !=''):
                line = config.readline()
                if(line[0] == '/'):
                        result = line[0:-1]
                        break
        config.close()
        if (result == None):
                raise ValueError("no path found")
        return result

###
# genDefaultConf
# IN : None
# OUT: None
# DO : create a default config file for musicator
###
def genDefaultConf():
        config = open(os.getenv("HOME")+"/.musicatorrc", 'w')
        config.write("# give the absolute path to your playlists (without sharps)\n")
        config.write("# example : \n")
        config.write("# /home/<your user name>/playlist")
        config.close

###
# main
###
if (__name__ == "__main__"):
        argc = len(sys.argv)
        program = "/usr/bin/mplayer"
        if (os.access(os.getenv("HOME")+"/.musicatorrc", os.F_OK)):
                path2playlist = readConfigFile()
        else:
                print("config file don't exist.")
                print("generating ~/.musicatorrc ...")
                genDefaultConf()
                print("~/.musicatorrc successfully generated !")
                print("please wrote your playlist path on it to use musicator !")
                sys.exit(0)

        if (argc < 2 or argc > 3):
                usage(sys.argv[0])

        elif(argc == 2):
                if(sys.argv[1] != "-show"):
                        usage(sys.argv[0])
                else:
                        (showPlaylist(path2playlist))
        else:
                if( sys.argv[1] != "-launch"):
                        usage(sys.argv[0])
                else:
                        if(inList(sys.argv[2], path2playlist)):
                                playlist = path2playlist+sys.argv[2]
                                os.execl(program, program, "-playlist", playlist, "-shuffle")

                                ################
                                #     BOUH !   #
                                # \|/ ____ \|/ #
                                # "@'/ ,. \'@" #
                                # /_| \__/ |_\ #
                                #    \__u_/    #
                                #              #
                                ################

