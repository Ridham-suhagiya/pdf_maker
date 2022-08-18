
def pdfmaker(paths,pdf):
    
     
    for i in range(len(paths)):
        pdf.add_page()
        
        # height,weidth = dimensions[i]       ## 1128, 800  -- > 210 , 290  
        # height  = height//5.37
        # weidth = weidth // 2.75


        pdf.image(paths[i],0,0,210,290)
    pdf.output("./test.pdf","F")
 