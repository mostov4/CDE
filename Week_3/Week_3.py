'''
    Scraply Spider
    IP switching/Proxy

    link contains data about the site

'''
from bs4 import BeautifulSoup
import requests
html_doc = '''<article class="product_pod">
   <div class="image_container">
      <a href="in-her-wake_980/index.html"><img src="../media/cache/5d/72/5d72709c6a7a9584a4d1cf07648bfce1.jpg" alt="In Her Wake" class="thumbnail"></a>
   </div>
   <div id="img_container" custom_attr="cus_attr">
      <a href="in-her-wake_980/index.html"><img src="../media/cache/5d/72/newimage.jpg" alt="On the tree" class="thumbnail"></a>
   </div>
   <p class="star-rating One">
      <i class="icon-star"></i>
      <i class="icon-star"></i>
      <i class="icon-star"></i>
      <i class="icon-star"></i>
      <i class="icon-star"></i>
   </p>
   <h3><a href="in-her-wake_980/index.html" title="In Her Wake">In Her Wake \n</a></h3>
   <div class="product_price">
      <p class="price_color">£12.84</p>
      <p class="instock availability">
         <i class="icon-ok"></i>
         In stock
      </p>
      <form>
         <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
      </form>
   </div>
</article>'''

soup = BeautifulSoup(html_doc,'html.parser')

soup.select('div')

soup.select_one('div')

soup.select_one('h3 a').attrs

soup.select_one('h3 a').text

soup.select_one('h3 a').text.strip()

soup.select('div')

soup.select('div.image_container')

soup.select('div')

required_div = soup.select('div.image_container')
required_div

required_div = soup.select_one('div#image_container')
# hash # means telling id, iterating through id

soup.select('div p.price_color')

soup.select_one('p.price_color').text

soup.select_one('div p.price_color').text

#check for loop logic in sir's file

soup.find_all(name='div', id="image_container") #shouldnt this print?

soup.find(name='div',attrs={"class":"image_container"})

""" Download extension selector lib from google chrome store"""
