import birdfeeder 
import ujson 
import sys 

stats = birdfeeder.user_stats(screen_name = "newslynx")
sys.stdout.write(ujson.dumps(stats))