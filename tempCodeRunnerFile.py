if photo_img:
    web_button = tk.Button(scr, image=photo_img, command=Web, bg="#505a5b", width=40, height=20)
    web_button.place(x=140, y=5)
else:
    web_button = tk.Button(scr, text="Web", command=Web, bg="#505a5b", fg="#000000", width=5, height=1)
    web_button.place(x=140, y=5)
