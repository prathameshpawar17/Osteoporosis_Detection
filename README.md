Assessment of osteoporotic disease from the radio-graph image is a significant challenge. 
Texture characteristics when observed from the naked eye for the bone micro-architecture of the 
osteoporotic and healthy cases are visually very similar making it a challenging classification problem .To 
extract the discriminative patterns in all the orientations and scales simultaneously in this study we have 
proposed an approach that is based on a combination of multi resolution Gabor filters and 1D local binary 
pattern (1DLBP) features. Gabor filter are used due to their advantages in yielding a scale and orientation 
sensitive analysis whereas LBPs are useful for quantifying microstructural changes in the images. Our 
experiment show that the proposed method shows good classification results with an overall accuracy of 
about 72.71% and outperforms the other methods that have been considered in this paper.
Index Terms— Texture analysis, Pattern recognition, Gabor filters, Osteoporosis.
• Keywords:
• Osteoporosis.
• Menopause.
• Bone density.
• Bisphosphonates.
• Bone fracture.
• Osteopenia.
• Falls.
• Hip fracture
Introduction :
Osteoporosis is a bone condition caused by reduction in bone mass and degeneration of bone structure, 
that leads to high susceptibility to fragility fractures. Osteoporosisrelated fracture is a major global 
health risk, affecting one in three women and one in five men over the age of 50. According to the AsiaPacific Regional Audit in 2013, osteoporosis accounts for more hospitalization than diabetes, myocardial 
infarction and breast cancer, in women above the age of 45 years [1]. It is more prevalent among the 
elderly population, especially postmenopausal women [2]. With rise in aging population, there will be a 
substantial rise in incidence of fractures. It is projected that by 2050, at least one-third of the world 
population will be aged over 50 years and in Asia alone, a 7.6-fold increase in ageing population is 
expected, that may result in more than 50% of the global fractures to occur in Asia [1]. Osteoporosis is a 
silent disease, being painless and asymptomatic and it often goes undiagnosed until a fragility fracture


how to run web interface:
step 1) Open Anaconda prompt-type jupyter notebook (hit enter)
step 2) Open Onedrive->desktop->documents->osteoporosis_detection->flask->model.ipunb
step 3) click on Kernel option->click on restart and run all

After the completion of jupyter pgm
step 4) open another anaconda prompt window
we have to reach to our python app.py file so we can go one by one or by copying the path
1st method :(hit enter after each step)
1)cd Onedrive
2)cd Desktop
3)cd osteoporosis_detection
4)cd flask
5)python app.py 
copy url displayed on the screen and paste in the browser

2nd method:
go to desktop->osteoporosis_detection->flask
now copy the path and paste into anaconda prompt by adding cd before the path
then write python app.py 
now copy the url displayed on the screen.

note:copy the url only once otherwise it quit.


Connecting the database to the web interface
step1)go to desktop->osteoporosis_detection->flask->database->click in the path and type cmd and hit enter
step 2) A command prompt will be open on the screen then write sqlite3 Medical.db
step 3)now type .databases
step 4) type .tables then you can see created table names
step 5)if you have to fetch details filled by the user simply type the command as :select * from user_details;
select * from user_feedback;
and you can 
delete from user_details;
delete from user_feedback;

