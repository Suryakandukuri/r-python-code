Condition to check is that all the columns should have same name.
==========================================================
setwd("C:/Users/sstka/Documents/Factly/Domestic Aircraft")

library(readxl)
library(xlsx)

mypath<-"C:/Users/sstka/Documents/Factly/Domestic Aircraft"

filenames=list.files(path=mypath)

DF <-  read_excel(filenames[1])

#reading each file within the range and append them to create one file
for (f in filenames[-1]){
  df <- read_excel(f)      # read the file
  DF <- rbind(DF, df)    # append the current file
}
#writing the appended file  
write.csv(DF, "completefile.csv", row.names=FALSE, quote=FALSE)

#or write it to an excel file


write.xlsx(DF,"C:/Users/sstka/Documents/Factly/Domestic Aircraft/newcompletefile.xlsx")