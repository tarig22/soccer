
import requests

def getData():
#     url = requests.get("https://www.as-goal.com/m/").text
    url = requests.get("https://www.google.com/search?q=litcoin&client=opera&hs=iVo&sxsrf=AOaemvL-0i0cX8nesXXY5vBQ0tO7-owVAA%3A1630105014593&ei=tm0pYdLTI8b4sAfVrKfwBQ&oq=lit&gs_lcp=Cgdnd3Mtd2l6EAEYADIJCCMQJxBGEIICMgsILhCABBDHARCjAjIFCAAQgAQyBQguEIAEMgUILhCABDIFCC4QgAQyBQguEIAEMgUILhCABDIFCAAQgAQyBQgAEIAEOgcIABBHELADOgQIIxAnOgYIIxAnEBM6CgguEMcBENEDEEM6BAgAEENKBAhBGABQ5fI5WOb2OWDjhTpoA3ACeACAAaMCiAGBBpIBAzItM5gBAKABAcgBCMABAQ&sclient=gws-wiz").text
    x = url.find("<div id=\"Today\"")
    y = url.find("<div id=\"Tomorrow\"")
    return len(url[x:y])


print(getData())
