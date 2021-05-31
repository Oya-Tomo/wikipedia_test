import wikipediaapi

My_wiki = wikipediaapi.Wikipedia("jp")

res = My_wiki.page("wikipedia")

if res.exists() == False:
  print("検索ワードを変更してください。")
else:
  print(res.text)
