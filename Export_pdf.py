from packages import *
from visualize_plots_window import *


def export_to_pdf(self,plots_data,data):
    """Export plots and summary to a PDF with proper error handling."""
    focus_text,cognitive_text,relaxation_text=self.get_summary_text(data)
    # if plots_data.keys():
    #     if 'Focus' not in plots_data.keys():
    #         self.canvas.toolbar.home()
    #         self.generate_dummy_data( 'Focus',data,focus_text,draw=0)
    #     if 'Cognitive load' not in plots_data.keys():
    #         self.canvas.toolbar.home()
    #         self.generate_dummy_data( 'Cognitive load',data,cognitive_text,draw=0)
    #     if 'Relaxation' not in plots_data.keys():
    #         self.canvas.toolbar.home()
    #         self.generate_dummy_data( 'Relaxation',data,relaxation_text,draw=0)
    # else:
    self.canvas.toolbar.home()
    self.generate_dummy_data( 'Focus',data,focus_text,draw=0)
    self.generate_dummy_data( 'Cognitive load',data,cognitive_text,draw=0)
    self.generate_dummy_data( 'Relaxation',data,relaxation_text,draw=0)
    
    try:
        #Get save location with proper extension handling
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save PDF", "", "PDF Files (*.pdf);;All Files (*)"
        )
        if not file_path:  # User canceled the operation
            return
        
        if not file_path.endswith(".pdf"):
            file_path += ".pdf"



        # Define PDF properties
        doc = canvas.Canvas(file_path, pagesize=A4,rightMargin=20,
            leftMargin=20,
            topMargin=72,
            bottomMargin=72)
        width, height = A4
        right=20

        doc.setFillColorRGB(0.05,0.05,0.05)
        doc.rect(0, 0, width, height, fill=True, stroke=False)


        # print(width,height)
        # Set background color (light gray as an example)
        heading_height=check_height(doc,height-50,0.5)
        ################## heading orbit report#####################
        font_name="Helvetica"
        doc.setFillColor(white)
        doc.setFillAlpha(0.5)
        doc.setFont("Helvetica", 10)
        title_text = "O R B I T   R E P O R T"
        doc.drawString(right,heading_height, title_text)  # Top position
        
        doc.setFillAlpha(1)
        doc.setFont("Helvetica-Bold", 11)
        stellar_text = "N E U R O S T E L L A R"
        text_width=width - stringWidth(stellar_text,font_name,11)-15
        doc.drawString(text_width,heading_height,stellar_text)
        # doc.drawImage('assests/logo_2.png',text_width-25,heading_height-10,width=20,height=20)  # Top position

        ############# name of the person ##########33
        
        doc.setFont("Helvetica", 16)
        subtitle_text = "Hi Kenny!"
        name_height=check_height(doc,heading_height-30,1)
        doc.drawString(right, name_height, subtitle_text)


        # ############## basic intro sentences ##########
        # doc.setFillAlpha(0.6)
        intro_height=check_height(doc,name_height-25,1)
        # text_object = doc.beginText(right, intro_height)
        # text_object.setFont(font_name, 12)
        # line_spacing=14
        # text_object.setLeading(line_spacing)  # Line spacing
        
        intro_text = """Here’s a detailed analysis from your session, showing how you adapt to challenges, maintain attention,
        and recover between demanding moments. Let’s dive in"""
        text_height_used=wrap_the_text(doc,intro_text,0.6,font_name,12,15,right,y_position=intro_height,max_width=width-30,char_spacing=0.3)
        # print(text_height_used)


        ########### activity tracking ###########
        doc.setFillAlpha(0.5)
        doc.setFont("Helvetica", 12)
        activity_text = data['SessionType']
        new_y_position = check_height(doc,text_height_used - 40,0.5)
        doc.drawString(right, new_y_position, activity_text)

        doc.setFillAlpha(1)
        doc.setFont("Helvetica", 13)
        activity_position=check_height(doc,new_y_position-25,1)
        doc.drawString(right,activity_position,"Playing Music") ################# variable


        ######### Tracking duration #########
        doc.setFillAlpha(0.5)
        doc.setFont("Helvetica", 12)
        doc.drawString(width/2, new_y_position, "TRACKING DURATION")

        doc.setFillAlpha(1)
        doc.setFont("Helvetica", 13)
        doc.drawString(width/2,activity_position,data['Duration']) ############# variable

        doc.setFillAlpha(0.5)
        doc.setFont("Helvetica", 13)
        date_position=check_height(doc,activity_position-25,0.5)
        doc.drawString(width/2,date_position,"27th Jan 2025") ############### varaible

        
        ################ about the session #######3333
        doc.setFillAlpha(0.5)
        doc.setFont("Helvetica", 12)
        about_position=check_height(doc,date_position-50,0.5)
        doc.drawString(right,about_position,"ABOUT THIS SESSION")
        
        content_position=check_height(doc,about_position-35,0.5)

        session_content_text = """This session reveals how you manage mental engagement and recovery throughout the task. By comparing your real-time brain activity to your baseline, we can see how effectively you balance focus, effort, and relaxation. The data highlights your ability to stay engaged, adapt to challenges, and recover when needed, ensuring optimal performance without mental fatigue"""

        next_y_position=wrap_the_text(doc,session_content_text,0.8,font_name,14,21,right,content_position,max_width=width-30,char_spacing=0.1)

        line_y=check_height(doc,next_y_position-40,0.8)
        faded_line(doc=doc,line_y=line_y,width=width)

        doc.setFillAlpha(0.7)
        baseline_position = check_height(doc,line_y - 45,0.7)
        baseline_txt="KNOW ABOUT YOUR REFERENCE LINE (BASELINE)"
        baseline_font_width=16
        text_object = doc.beginText()
        text_object.setTextOrigin((width - stringWidth(baseline_txt,font_name,baseline_font_width))/2-right, baseline_position) 
        text_object.setFont("Helvetica", baseline_font_width)
        text_object.setCharSpace(1.8)  # Adjust character spacing (increase value for more spacing)
        text_object.textLine(baseline_txt)  # Add text
        doc.drawText(text_object)  # Draw the text on the PDF



        baseline_content_position=check_height(doc,baseline_position-40,0.5)
        baseline_content_txt="The baseline represents your brains natural state before the session, serving as a reference to measure changes in Focus, Cognitive Load, and Relaxation. It helps us understand how your brain responds to challenges by comparing real-time data to your starting point."
        note_position=wrap_the_text(doc,baseline_content_txt,0.4,font_name,14,21,right,baseline_content_position,width-30)


        note_txt="Note: The above data is trimmed to 300 seconds (5 minutes) to highlight the dynamics within this timeframe"
        doc.setFillAlpha(0.5)
        text_object = doc.beginText()
        note_font_width=9
        text_object.setTextOrigin((width - stringWidth(note_txt,font_name,note_font_width))/2-right, check_height(doc,note_position-40,0.6))  # Set text
        text_object.setFont("Helvetica", note_font_width)
        text_object.textLine(note_txt)
        doc.drawText(text_object)

        

        ########################## focus heading ###################

        focus_heading_position=check_height(doc,200,0.5)
        focus_content_position=check_height(doc,focus_heading_position-40,0.5)
        focus_txt="""Focus is measured by analyzing linked to and goal-directed tasks. The focus starts at a moderate level (~44), suggesting the user is engaged but not fully immersed initially. It gradually increases, peaking (~70) as the user becomes more attentive or encounters something mentally stimulating or challenging. While there are slight dips later on, focus remains relatively high, indicating consistent engagement with the task despite minor shifts in attention.
        """

        height_1=plots_with_content(doc,"FOCUS",focus_txt,right,focus_heading_position,focus_content_position,width,fig=plots_data['Relaxation'],char_spacing=0.2)

        cognitive_heading_posiiton=check_height(doc,height_1-60,0.5)
        cognitive_content_position=check_height(doc,cognitive_heading_posiiton-40,0.5)

        cognitive_txt="""Cognitive load is evaluated using the . Theta waves (4–8 Hz) increase during working memory use, while beta waves increase with higher engagement. Cognitive load stays moderate (~30 45) throughout, reflecting a steady level of Peaks in cognitive load often overlap with high focus scores, indicating moments where the user is processing something complex or challenging .The relative stability of cognitive load, with only slight dips, suggests the task is demanding but manageable overall."""


        height_2=plots_with_content(doc,"COGNITIVE LOAD",cognitive_txt,right,cognitive_heading_posiiton,cognitive_content_position,width,fig=plots_data['Cognitive load'],char_spacing=0.2)

        relaxation_heading_posiiton=check_height(doc,height_2-60,0.5)
        relaxation_content_position=check_height(doc,relaxation_heading_posiiton-40,0.5)

        relaxation_txt="""Relaxation is calculated by monitoring waves, which dominate in. The relaxation score starts relatively high (~41–57), showing the user is calm and comfortable at the beginning. Over time, relaxation gradually decreases, with noticeable dips. This could mean the task is becoming more demanding or slightly stressful as it progresses. Occasional recoveries suggest moments where the user feels at ease, possibly during simpler or more familiar parts of the task. The downward trend toward the end could reflect growing mental fatigue or increased effort in handling the task."""
        
        height_3=plots_with_content(doc,"RELAXATION",relaxation_txt,right,relaxation_heading_posiiton,relaxation_content_position,width,fig=plots_data['Relaxation'],char_spacing=0.2)

        faded_line_2_position=check_height(doc,height_3-40,0.5)
        faded_line(doc=doc,line_y=faded_line_2_position,width=width)



        

        # final_position=wrap_the_text(doc,note_txt,0.5,font_name,7,20,right,check_height(doc,next_note_position-20,0.5),width-30)
        # # Save the document
        doc.save()

        # Inform the user of success
        QMessageBox.information(
            self,
            "Success",
            f"PDF successfully exported to:\n{file_path}"
        )
        try:
            # Open PDF with the default application
            if sys.platform == 'win32':
                os.startfile(file_path)
        except Exception as e:
            print(f"Error opening PDF: {str(e)}")


        # Clean up the temp file
        # if os.path.exists(temp_plot_path):
        #     os.remove(temp_plot_path)

    except Exception as e:
        QMessageBox.critical(
            self,
            "Error",
            f"Error exporting PDF:\n{str(e)}"
        )
def wrap_the_text(doc,wrapped_text,alpha_value,font,font_size,line_spacing,right,y_position,max_width,char_spacing=0):
    

    ############## session content #########3
    doc.setFillAlpha(alpha_value)
    content_height=y_position
    text_object = doc.beginText(right, content_height)
    text_object.setFont(font, font_size)
    text_object.setLeading(line_spacing)  # Line spacing
    
    text_object.setCharSpace(char_spacing)

    line = ""
    for word in wrapped_text.split():
        # Measure line width with new word added
        test_line = line + " " + word if line else word
        text_width = stringWidth(test_line, font,font_size) +(len(test_line)-1) * char_spacing
        if text_width < max_width:  # If fits within width, add word to line
            line = test_line
        else:
            text_object.textLine(line)  # Draw current line
            content_height-=line_spacing
            check_val=check_height(doc,content_height,alpha_value)
            if check_val!=content_height:
                updated_height=wrap_the_text(doc,wrapped_text,alpha_value,font,font_size,line_spacing,right,check_val,max_width,char_spacing=char_spacing)
                return updated_height

            line = word  # Start new line

    # Add the last remaining line
    if line:
        text_object.textLine(line)
    text_object.setCharSpace(0)
    doc.drawText(text_object)
    return content_height

def faded_line(doc,line_y,width):
    page_width=width
    num_steps = 1000  # More steps = smoother transition
    line_height = 2  # Line thickness

    for i in range(num_steps):

        alpha_more=0.08

        if int(num_steps*0.01)>i and int(num_steps*0.99)<i:
            alpha_more=0.1
        alpha = (i / num_steps)*alpha_more # Gradually increasing opacity from 0 to 1

        if alpha>0.5*alpha_more:
                alpha=alpha_more-alpha
        x_position = 60 + (i / num_steps) * (page_width - 100)  # Spread across width
        
        doc.setFillColorRGB(1, 1, 1, alpha)  # White color with transparency
        doc.rect(x_position, line_y, 3, line_height, fill=1, stroke=0) # Slight vertical shift
def plots_with_content(doc,heading_txt,content_txt,right,heading_position,content_position,width,fig,char_spacing=0.5):
    

    width,page_height=doc._pagesize
    font_size=doc._fontsize
    doc.showPage()
    doc.setFont("Helvetica",font_size)
    doc.setFillColorRGB(0.05,0.05,0.05)
    doc.rect(0, 0, width, page_height, fill=True, stroke=False)
    doc.setFillColor(white)
    doc.setFillAlpha(0.5)
    if heading_txt=='FOCUS':
        performance_position = check_height(doc,page_height - 50,0.5)
        performance_txt="PERFORMANCE METRICS"
        performance_font_width=15
        text_object = doc.beginText()

        text_object.setTextOrigin((width - stringWidth(performance_txt,'Helvetica',performance_font_width))/2-right, performance_position)  # Set text position
        text_object.setFont("Helvetica", performance_font_width)
        text_object.setCharSpace(1.8)  # Adjust character spacing (increase value for more spacing)
        text_object.textLine(performance_txt)  # Add text

        doc.drawText(text_object)  # Draw the text on the PDF
        
        text_object.setCharSpace(0)  # Reset to default spacing
        doc.drawText(text_object)
        height=performance_position-50
    else:
        height=page_height-50
    doc.setFillAlpha(0.5)
    doc.setFont("Helvetica", 12)
    doc.drawString(right,height,heading_txt)
    
    
    img_buffer = BytesIO()
    fig.savefig(img_buffer, format='png', dpi=150, bbox_inches='tight')
    img_buffer.seek(0)
    
    # Add title
    
    # Add plot image
    img_read = ImageReader(img_buffer)
    y_value=check_height(doc,height-300,alphaValue=0)
    doc.drawImage(img_read,right,y_value,width=width-50,height=290)

    heigth_after_content=wrap_the_text(doc,content_txt,0.5,"Helvetica",14,21,right,y_value-30,width-30,char_spacing=char_spacing)
    return heigth_after_content
def check_height(doc,height,alphaValue):
    if height<50:
        width,page_height=doc._pagesize
        font_size=doc._fontsize
        doc.showPage()
        doc.setFont("Helvetica",font_size)
        doc.setFillColorRGB(0.05,0.05,0.05)
        doc.rect(0, 0, width, page_height, fill=True, stroke=False)
        doc.setFillColor(white)
        doc.setFillAlpha(alphaValue)
        height=page_height-50
    return height


