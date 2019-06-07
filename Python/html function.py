"""Write the html_list function. The function takes one argument, a list of strings, and returns a single string which is an HTML list. For example, if the function should produce the following string when provided the listul>
<li>first string</li>
<li>second string</li>
</ul>
That is, the string's first line should be the opening tag <ul>. Following that is one line per element in the source list, surrounded by <li> and </li> tags. The final line of the string should be the closing tag </ul>."""

#define the  html_list function
def html_list(str):
    
    for items in range(len(str)):
        itemsnew="<li>"+items+"</li>"
    first_item="<ul>\n" +itemsnew+"\n</ul>"
    return first_itemlen


print (html_list(['first string', 'second string']))


