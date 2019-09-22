from webscrap import wlog
from webscrap import wscrap
import facebook
wlog.set_custom_log_info('html/error.log')

try:
    raise Exception
except Exception as e:
    wlog.report(str(e))


fb_scrap=wscrap.FBScraper(wscrap.fb_url,wlog)                     # call FBScraper classs 
#fb_scrap.write_webpage_as_html()                                  # call method for writing scrap data to html    
fb_scrap.read_webpage_from_html()                                 # call method for reading data from html file
fb_scrap.convert_data_to_bs4()                                    # call method for converting data to beautiful soup
fb_scrap.parse_soup_to_csv()                                      # call method for parsing soup data to csv
