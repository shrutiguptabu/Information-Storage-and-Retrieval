import Classes.Path as Path
import re
# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class TrectextCollection:

    def __init__(self):
        # 1. Open the file in Path.DataTextDir.
        try:
            # open the file with UTF-8 encoding
            self.fileReader = open(Path.DataTextDir, encoding="utf8")
        except IOError:
            print('Unable to open the Trectext file')
            
        return

    def nextDocument(self):
        # 1. When called, this API processes one document from corpus, and returns its doc number and content.
        
        # define the empty content variable
        content = []
        docNo = ""
        
        # Set the flag for content started to false
        beginContent = False
        
        # Read the first line
        line = self.fileReader.readline()
        
        # 2. When no document left, return null, and close the file.
        if not line:
            self.fileReader.close()
            return None
        
        # Iterate through file, line by line until we hit closing tag or eof
        while(line):
            
            # if this is the ending tag, break out of the loop
            if("</DOC>" in line):
                break
            
            # if this is the content end tag, set the content flag to false
            if("</TEXT>" in line):
                beginContent = False
            
            # Start extracting the content if beginContent is true
            if (beginContent):
                content.append(line)
            
            # Check if we have the begin content tag
            if ("<TEXT>" in line):
                beginContent = True   
            
            # Extract DOCNO if found
            if ("<DOCNO>" in line):
                docNo = re.search("<DOCNO>(.*)</DOCNO>",line).group(1)
                #docNo = docNo.group(1)
                
            # Read a new line to be processed in next iteration
            line = self.fileReader.readline()

        # Return docNo and content in a list object
        return [docNo, "".join(content)]
