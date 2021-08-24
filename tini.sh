#!/bin/bash

function tini(){
  cd ~/dev/tini
  . env/bin/activate
  python tini.py
  cd ~/dev
}