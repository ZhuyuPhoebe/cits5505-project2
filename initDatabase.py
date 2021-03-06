import sqlite3

conn = sqlite3.connect('cits.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS `chapters` (
  `ID` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `Title` varchar(225) NOT NULL,
  `Overview` text,
  `UnitID` INTEGER NOT NULL
);''')
conn.commit()
print ("Table chapters created successfully")

conn.execute('''INSERT INTO `chapters` (`ID`, `Title`, `Overview`, `UnitID`) VALUES
(1, 'The Web', '<para>\n When you surf the internet what types of things do you think occurs in the background? How does it know what to display? How does it know when you click or input items? All of these ''things'' are a result of a web system in which a web server and web client communicate with each other. Every single click and action can trigger a request to a web server that will return the desired result. There are so many components that go into a well designed web system and within this chapter you will be exposed to many of these fundamental concepts. \n </para>', 1),
(2, 'HTML5', '<para>\n Up until this point, we have learned about some of the background events that occur in a web system. But all of this doesn''t really matter if there is nothing for a user to see and interact with. In order to display a website to a user, HTML5 is used! If you have previous experience with programming languages such as C, C++, C#, and Java, you might think HTML should be a similar enough. Wrong! HTML5 is a markup language that specifies both the structure as well as the content of a web page. The syntax is quite unique compared to common object-orientated or scripting languages.\n </para>', 1),
(3, 'CSS3', '<para>\n Now that we know how to create the contents of a webpage, how do we make it look nicer than plain black and white text with no formatting? This is done using CSS, Cascading Style Sheets.\n </para><para>\n Although you can add formatting to an HTML5 directly with attributes, this can result in messy code. It also makes it difficult to make any uniform change to the same element for example (unnecessary duplicaate formatting). For example, you want all headers to be blue but done want to add that color attribute to every single element in all of your files. CSS takes care of all formatting in a seperate file where you can easily control all of the same elements'' styling.\n </para><para>\n In order to link a style sheet to your HTML5 file, you need to add the following line within the head element. &lt;link rel="stylesheet" type="text/css" href="filePath.css"&gt;. Now you may begin creating your .css file that will help format your web page\n </para>', 1),
(4, 'JavaScript', '<para>\n Now that you know the basics of HTML5 and CSS3, you might be wondering how to do things like calculations, event handling, or creating a dynamic web page. This is where Javascript can improve your web pages greatly. This is not the same as Java which is object orientated. Javascript is a scripting language to enhance both the appearance and functionality of web pages.\n </para>', 2),
(5, 'HTML5 Canvas', '<para>\n The canvas element is used to create 2D graphics, animation, images, videos. This is where you can let your creativity shine with more artistic elements. The canvas works with a grid system of (x horizontal, y vertical). top left corner has the grid value of (0,0). Moving right will increase the x value (ie. (50,0) is 50 pixels to the right of the top left corner). Moving down will increase the y coordinate (ie. (50,10) is 50 px right and 10 px down from the left corner).\n </para>', 2),
(6, 'XML', '<para>\n XML stands for Extensible Markup Language. It has become a standard format for data exchange over the internet. This markup language can describe any type of data that humans can understand and computers to easily process. Below is an example of XML describing a baseball player (Detail p.512).\n <image src="../static/img/fig15-1_p512.png">\n Simple XML Example\n </image>\n <para>\n The structure of XML is similar to HTML5 elements and can even have attributes. The ''tags'' in this case are user defined and therefore there are endless possibilities in representing data.\n </para>\n </para>', 3),
(7, 'AJAX', '<para>\n Ajax stands for Asynchronous Javascript and XML. This makes client side scripting more responsive to your web system. It send aynchronous request to the server and will not be blocked, therefore making your webpages more responsive.\n </para><para>\n Traditionally, a web system has a client side and server side. Ajax is considered to be a middle tier between the the client and server. Ajax can create a XMLHttpRequest to manage a request and retrieve the data from the server. While this request has been sent, the user is able to move on. A good aspect of using Ajax is that it does not require you to reload a page every time a request is sent. It uses a function known as the <a class="def">callback function</a> that uses <a class="def">partial page update</a> which will update the specific element rather than the whole page.\n </para><para>\n The following image (Detail p.574) gives some insight of how Ajax works.\n </para><image src="../static/img/fig16-2_p574.png">\n Intro to AJAX\n </image>', 3);''')

conn.commit()
print ("chapters Records Insert successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS `questions` (
  `ID` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `Question` varchar(225) NOT NULL,
  `QuizID` INTEGER NOT NULL,
  `Type` INTEGER NOT NULL
);''')
conn.commit()
print ("Table questions created successfully")

conn.execute('''INSERT INTO `questions` (`ID`, `Question`, `QuizID`, `Type`) VALUES
(1, 'What does HTML5 stand for?', 1, 0),
(2, 'What is true about the Web Server', 1, 0),
(3, 'What are the three tiers in order from bottom tier to top tier in a Web System?', 1, 0),
(4, 'CSS stands for?', 1, 0),
(5, 'What does the head element used for?', 1, 0),
(6, 'Are URIs the same as URLs? Why?', 1, 0),
(7, 'How can you stylize your HTML5 files?', 1, 0),
(8, 'Is Javascript the same as Java?', 2, 0),
(9, 'What does DOM stand for?', 2, 0),
(10, 'What are the purpose of semi colons?', 2, 0),
(11, 'What is the result of "y + 5 = " + y + 5, when y = 1?', 2, 0),
(12, 'How do you get the result "x + 10 = 30", when x = 20?', 2, 0),
(13, 'How can you trigger an event?', 2, 0),
(14, 'Where is (0, 0) on the HTML5 Canvas element', 2, 0),
(15, 'What does XML stand for?', 3, 0),
(16, 'What types of elements can I use in an XML file?', 3, 0),
(17, 'What is the most common way to validate XML documents?', 3, 0),
(18, 'How does one stylize an XML document?', 3, 0),
(19, 'What does AJAX stand for?', 3, 0),
(20, 'What is a favourable aspect of using Ajax?', 3, 0),
(21, 'What status code represents a successful request?', 3, 0),
(22, 'When sending a (  ) request, the client intent is to be able to modify the data contained in the server.', 1, 1),
(23, 'Within the starting tag of an element, you can specify properties of the element using (  ).', 1, 1),
(24, 'These are known as the Document Object Model (  ) which we will later discuss how to get elements and attributes for these objects.', 2, 1),
(25, 'You can either use a inline functions, global elements, or use (  ) to invoke these methods.', 2, 1),
(26, '(  ) stands for Document type definition.', 3, 1),
(27, '(  ) is commonly used through XMLHttpRequests, which is request manager objects.', 3, 1);''')
conn.commit()
print ("questions Records Insert successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS `quiz` (
  `ID` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `Title` varchar(225) NOT NULL,
  `UnitID` INTEGER NOT NULL
);''')
conn.commit()
print ("Table quiz created successfully")

conn.execute('''INSERT INTO `quiz` (`ID`, `Title`, `UnitID`) VALUES
(1, 'Unit 1 Quiz', 1),
(2, 'Unit 2 Quiz', 2),
(3, 'Unit 3 Quiz', 3);''')
conn.commit()
print ("quiz Records Insert successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS `quizanswers` (
  `ID` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `Answer` varchar(225) NOT NULL,
  `Correct` INTEGER NOT NULL,
  `QuestionID` INTEGER NOT NULL
);''')
conn.commit()
print ("Table quizanswers created successfully")

conn.execute('''INSERT INTO `quizanswers` (`ID`, `Answer`, `Correct`, `QuestionID`) VALUES
(1, 'HTTP Text Markup Language', 0, 1),
(2, 'Hypertext Markup Language', 1, 1),
(3, 'HTTP Text Markup Lookup', 0, 1),
(4, 'Hypertext Markup Lookup', 0, 1),
(5, 'It sends requests to retrieve information files', 0, 2),
(6, 'It is a physical room of people who receive data and finds it', 0, 2),
(7, 'It is not a part of web systems', 0, 2),
(8, 'It receives requests for information and data', 1, 2),
(9, 'Database, GUI Layer, Business layer', 0, 3),
(10, 'GUI layer, Business Layer, Database', 0, 3),
(11, 'Business Layer, Database, GUI Layer', 0, 3),
(12, 'None of the above', 1, 3),
(13, 'Cascading Sheet System', 0, 4),
(14, 'Common Sheet Style', 0, 4),
(15, 'Cascading Style Sheet', 1, 4),
(16, 'Creative Styling Size', 0, 4),
(17, 'The content of the web page (ie. images, text, headings)', 0, 5),
(18, 'The title, encoding, and css linking', 1, 5),
(19, 'All headings of the document go here', 0, 5),
(20, 'Specifies what elements have been used in the document', 0, 5),
(21, 'No, they are synonyms to each other', 0, 6),
(22, 'Yes, URIs are a subset of URLs', 0, 6),
(23, 'Yes, URLs are a subset of URIs', 1, 6),
(24, 'Yes, URIs are integer based and URLs are long int based', 0, 6),
(25, 'From within the HTML5 file', 0, 7),
(26, 'In a CSS file', 0, 7),
(27, 'None of the above', 0, 7),
(28, 'All of the above', 1, 7),
(29, 'No, one is a computer language and another is a coffee type', 0, 8),
(30, 'No, one is a web scripting language and the other is object orientated', 1, 8),
(31, 'Yes, Javascript is special type of Java', 0, 8),
(32, 'Yes, Java is a special type of Javascript', 0, 8),
(33, 'Document Object Model', 1, 9),
(34, 'Data Objective Model', 0, 9),
(35, 'Document Ordered Model', 0, 9),
(36, 'Data Object Manager', 0, 9),
(37, 'They are ignored so you can put them anywhere', 0, 10),
(38, 'They are not required but terminate a line', 1, 10),
(39, 'They are absolutely required to terminate a line', 0, 10),
(40, 'They are special characters and should not be used', 0, 10),
(41, '"y + 5 = 6"', 0, 11),
(42, '"y + 5 = y + 5"', 0, 11),
(43, '"y + 5 = y5"', 0, 11),
(44, '"y + 5 = 15"', 1, 11),
(45, '("x + 10 = ") + x + 10', 0, 12),
(46, '"x + 10 = " + (x) + 10', 0, 12),
(47, '"x + 10 = " + (x + 10)', 1, 12),
(48, '("x + 10") + (x) + (10)', 0, 12),
(49, 'With JQuery, $("#test").onclick = function() \{\}', 1, 13),
(50, 'With global javascript (ie. OnClick.Button() \{\});', 0, 13),
(51, 'With inline HTML5. Where special elements have the tag as the event trigger (ie. <onclick>)', 0, 13),
(52, 'All of the above', 0, 13),
(53, 'Top Right Corner', 0, 14),
(54, 'Center of the element', 0, 14),
(55, 'Bottom Left', 0, 14),
(56, 'Top Left', 1, 14),
(57, 'External Markup Language', 0, 15),
(58, 'External Management Language', 0, 15),
(59, 'Extensible Markup Language', 1, 15),
(60, 'Extensible Management Language', 0, 15),
(61, 'The same as those in HTML5', 0, 16),
(62, 'There is an online database of XML elements to use', 0, 16),
(63, 'XML documents do not use elements', 0, 16),
(64, 'Any elements can be used since they are user defined', 1, 16),
(65, 'XSD', 1, 17),
(66, 'XSL', 0, 17),
(67, 'DTD', 0, 17),
(68, 'DTL', 0, 17),
(69, 'Inline the XML sheet', 0, 18),
(70, 'With a XSL document', 1, 18),
(71, 'With a CSS document', 0, 18),
(72, 'With a HTML5 document', 0, 18),
(73, 'Abstract Javascript and XML', 0, 19),
(74, 'Asynchronous Javascript and XML', 1, 19),
(75, 'Adaptable Javascript and XML', 0, 19),
(76, 'Agile Javascript and XML', 0, 19),
(77, 'Ajax stylizes your web page with XML and Javascript', 0, 20),
(78, 'Ajax reloads your webpage quicker than without it', 0, 20),
(79, 'Ajax is not yet prefered or widely accepted', 0, 20),
(80, 'Ajax does not reload a web page after a request', 1, 20),
(81, '0', 0, 21),
(82, '100', 0, 21),
(83, '200', 1, 21),
(84, '500', 0, 21),
(85, 'POST', 1, 22),
(86, 'attributes', 1, 23),
(87, 'DOM', 1, 24),
(88, 'JQuery', 1, 25),
(89, 'DTD', 1, 26),
(90, 'Ajax', 1, 27);''')
conn.commit()
print ("chapters quizanswers Insert successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS `sections` (
  `ID` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `Title` varchar(225) NOT NULL,
  `Content` text,
  `ChapterID` INTEGER NOT NULL
);''')
conn.commit()
print ("Table sections created successfully")

conn.execute('''INSERT INTO `sections` (`ID`, `Title`, `Content`, `ChapterID`) VALUES
(1, 'Introduction', '<para>\n Before we dive into specific UI components and writing your first scripts, we will need to learn about some terms that will be mentioned throughout the unit.\n </para><definition term="Web Client">\n A web client sends its requests to the server and is usally known as the ''web browser''. As a user of a website, you are essential the web client. Some of these requests can include mouse-clicks, text input, and button-clicks.\n </definition><definition term="Web Server">\n A web server processes the client''s request and responds by either modifying and/or retrieving various forms of data. This can include requests to a database, server files, network files, and many others.\n </definition><definition term="HTTP">\n HTTP stands for HyperText Transfer Program, which is essentially what allows for the transfer of data between clients and servers. This all occurs over the internet/ intranet.\n </definition>', 1),
(2, 'HyperText Transfer Program (HTTP)', '<para>\n As defined in the previous section, HTTP enables the transfer and access of data. When you open up your browser and navigate to any website, you are most likely accessing HTML5 files, which creates the foundation of a website, using URIs and URLs. What exactly does this all mean? First, lets take a look the definition of these terms.\n </para><definition term="HTML5">\n HTML5 stands for HyperText Markup Language (v5 being the current major version). This language describes the content and framework of a webpage. Such content includes the text, images, formatting, and even some business logic. Using HTML5, you will be able to create .html or .htm files that will be the basics to any website.\n </definition><definition term="URI">\n URI stands for Uniform Resource Identifiers. In a general sense, it is a way to identify resources (i.e. web pages)on the internet.\n </definition><definition term="URL">\n URL stands for Uniform Resource Lookup and is actually a subset of URIs that not only identifies a resource but it also provides a method to locate the resource.\n </definition><para>\n Now that we have learned the terms, we need to understand the order of events that occur when accessing a web page.\n </para><para>\n In order for a web page to be displayed, there must be some commication performed between the client and the server. First, the client would request the resource (i.e. the user would type in a URL into a web browser) using HTTP. This will send a request to the address of webpage. The server would then receive this request and lookup the resource that was requested. After retrieving the resource, the server will respond by displaying resource and its contents. The following images, taken from Detail p.607-608, explains this process quite nicely.\n </para><image src="../static/img/fig17-1_p607-608.png">\n Figure 1. Web Server and Client Communication\n </image><para>\n As mentioned, the client can send many requests to the server. There are various request types such as GET and POST, to name a few.\n </para><definition term="GET">\n GET will asks the server to retrieve the data such as images or files. You can think of it as almost a ''read-only'' request that will not change any data stored on the server.\n </definition><definition term="POST">\n When sending a POST request, the client''s intent is to be able to modify the data contained in the server. This can include adding, deleting, and editing the server''s data. This usually involves data being sent from the client and processed by the server to obtain the desired result.\n </definition><para>\n With these flows of communication, a web system can become quite complex. In order to keep a web system maintainable and easy for other developers to understand, a multi-tier design architecture is often used. The most common multi-tier design is comprised of three distinct layers.\n </para><definition term="Database Layer (Bottom Tier)">\n Starting at the foundation of a web architecure is often a database level. This layer would typically hold all of the data a system contains to access, edit, and process. The client should never have direct access to this layer.\n </definition><definition term="Business Logic Layer (Middle Tier)">\n The middle tier of this design can be thought of as the middle man that processes the data in the bottom tier and hands it over to the top layer to display to the client. In this layer, algorithms, accessing data, and handling requests are performed. It is also very common for this layer to be split into two layers. One being a Database Access Layer and all other business logic.\n </definition><definition term="User Interface Layer (Top Tier)">\n At the top, is the UI layer that will present the data to the user. The most basic UI layer would simply be human readable but in order to make your web page stand out, a lot of UI elements and tricks are needed to creatively and effectively present the data.\n </definition><para>\n Now that we have learned the foundations of what occurs in a web system, we can look deeper into how to develop HTML5 files and design a attractive UI using CSS3.\n </para>', 1),
(3, 'Basics of HTML5', '<para>\n The most basic outline of an HTML5 file will be as follows (Detail p.39).\n </para><image src="../static/img/fig2-1_p39.png">HTML5 Outline</image><para>\n This is the skeleton that makes up any and all HTML5 files you view in a web browser today. We will quickly break down what the above file is composed of.\n </para><bulletList>\n <listItem>\n Line 1: This is the Document type, web browsers require this line in order for it to know what type of file it will be processing (compatibility etc.)\n </listItem>\n <listItem>\n Lines 2-3: These lines are comments and will be ignored by the browser\n </listItem>\n <listItem>\n Lines 6-9: This tag element is known as the Head. It contains the information of the HTML5 for the browser to properly know what to do with the file (encodings, title, style CSS, etc.)\n </listItem>\n <listItem>\n Lines 11-13: This is the Body, where all of a web page''s content is written.\n </listItem>\n </bulletList><para>\n To break down the terminology of the structures in an HTML5 file further, the following list will provide a basic syntax:\n </para><definition term="Element">\n As seen above, the head and body elements are required in every HTML5. An element is usually in the form &lt;tagname&gt;content&lt;/tagname&gt; (paragraphs, list items, headers, etc.). They can also be written without an end tag when no content is required and will be in the form &lt;tagname/&gt;\n </definition><definition term="Nested Elements">\n These are known as elements that fall within another element (ie. the title element at line 8)\n </definition><definition term="Attributes">\n Within the starting tag of an element, you can specify properties of the element using attributes. These follow the form attributeName="attributeValue". Common attributes include the class (grouping), id (unique identifier), and src (for images and other media).\n </definition>', 2),
(4, 'Common Elements', '<para>\n Like common objects and variable types in Java, C#, and python, HTML5 has many common elements that can be used in to build a web page. These are a few of the most common elements in HTML5\n </para><definition term="Headings">\n Have you noticed the various "titles" on this webpage and their varying sizes? Well that is the result of using the heading element, &lt;h1&gt;Title&lt;/h1&gt;Headings h1 (biggest) - h6 (smallest) are available to use. These act as titles that can help organize and display your web page<br/>\n </definition><example>\n <h3>Example h3 Title</h3>\n </example><definition term="Paragraphs">\n Just as the name suggests this element can create a paragraph of text &lt;p&gt;My paragraph&lt;/p&gt;\n </definition><example>\n <p>Example paragraph</p>\n </example><definition term="Links">\n You can make most elements act as clickable links using &lt;a href="http://google.ca"&gt;Google!&lt;/a&gt;.\n </definition><example>\n <a href="http://google.ca">Google!</a>\n </example><definition term="Images">\n Images, like the figures you have seen on this webpage, are shown using &lt;img src="pathToMyImg"&gt;. Note these do not need an end tag &lt;/img&gt; or a /&gt;\n </definition><definition term="Lists">\n You can make bulleted/unordered lists &lt;ul&gt; or numbered/ordered lists &lt;ol&gt;. Within these you create nested list item elements &lt;li&gt;\n </definition><example>\n <ol><li>list item 1</li><li>list item 2</li></ol>\n </example><definition term="Table">\n Tables are a bit more complex than the above elements. The general outline is as follows. You can look into addings headers and footers as they are quite straighforward.<br/>\n &lt;table&gt;<br/>\n &lt;tr&gt;Insert a row&lt;/tr&gt;<br/>\n &lt;th&gt;Column1&lt;/th&gt;<br/>\n &lt;th&gt;Column2&lt;/th&gt;<br/>\n &lt;/tr&gt;<br/>\n &lt;/table&gt;\n </definition><example>\n <table border="1px solid black">\n <tr><th>Banana</th><th>Yellow</th></tr>\n <tr><th>Apple</th><th>Red</th></tr>\n </table>\n </example><definition term="Form">\n This element helps to collect information from the user. This can also bundle together radio buttons and other elements together which requires user input. &lt;form&gt;Contains a lot of elements&lt;/form&gt;\n </definition><definition term="Input">\n As mentioned above these represent radio buttons, check boxes, text boxes, datetime, etc. &lt;input type="radio" name="grouping"&gt; Text\n </definition><example>\n <input type="radio" name="test"> Select Me!<br/></input>\n </example><para>\n The best way in my opinion to learning what you can do is to google and research! There are so many elements and neat tricks you can do with them in order to make your webpage truely interactive and better. Just remember in order for you to follow good coding rules you can should always validate your HTML5 file. This can be done <a href="https://validator.w3.org/">here</a>\n </para>', 2),
(5, 'General GuideLines', '<para>\n Similar to how there is so many attributes that you can do, it would be impossible for us to cover everything. However there is a general format that can be followed for the CSS styling. First we typically start with the tagname, class name, or id name in which we wish to stylize.\n </para><bulletList>\n <listItem>\n Tags can simply be written as they are (ie. h2 \{\})\n </listItem>\n <listItem>\n Classes need to being with a ''.'' (ie. .myClass {})\n </listItem>\n <listItem>\n IDs need to begin with ''#'' (ie. #uniqueTitle {})\n </listItem>\n </bulletList><para>\n You can also add multiple elements by comma seperating them (ie. h1, h2, #firstTitle {}) as well as follow a nested element such as a paragraph within the class "section"\n </para><example>\n .section p<br/>{<br/>}\n </example><para>\n Within the curly brackets is where you will add the attributes and their values. These follow the form attributeName: attributeValue;\n </para>', 3),
(6, 'Common Attributes', '<para>\n The following are a few common attributes that you can do with CSS\n </para><definition term="Color">\n You can set the value of the color attribute as a common color or an rgb hex value. The common colors can be written in plain english (ie. grey, red, green) and a list can be found <a href="https://www.w3schools.com/colors/colors_names.asp">here</a>. If you wish to use your own colours you may use the hex value with # appended in the beginning (ie. color: #00BFFF;)\n </definition><definition term="Width/Height">\n The size of an element can be modified. You can use various ways such as specifying the exact pixel (ie. 50px), relative to the font size (ie. 3em), percentage (ie. 50%), <a href="https://www.w3schools.com/cssref/css_units.asp">etc.</a>\n </definition><definition term="Margins/Padding">\n You can change the margins of the element or the padding in a similar way as the width and height\n </definition><definition term="Alignment">\n You can center, left, right, top, or bottom align. It is easiest in my opinion to text-align the containing element if you wish to, for example, center align the nested element.\n </definition><definition term="Border">\n You can change a border''s size and colour or even get rid of one (setting it to 0)\n </definition><definition term="Display">\n There are a few display attribute values you can use such as inline, inline-block, block, list-item, <a href="https://www.w3schools.com/cssref/pr_class_display.asp">etc.</a>\n </definition><para>\n The list goes on and on. Again, the best way in my opinion is to research what you want to do and how it can be doen with CSS!\n </para><conclusion>\n This concludes the tutorial on HTML5 and CSS. Please try out the quiz to test out your knowledge on this unit.\n </conclusion>', 3),
(7, 'Javascript Basics', '<para>\n Similar to CSS, you can have inline Javascript code within your HTML5 files or you can choose to have a seperate .js file and simply link it in your HTML5. In order to use Javascript inline you need to create a script element as follows (Detail p.187)\n </para><image src="../static/img/fig6-1_p187.png">\n Figure 1. Example of Javascript Element\n </image><para>\n In this example, a line was simply written to the document/ web page. If you would rather use javascript in a seperate file than you simply need to add ''&lt;script src="nameOfFile.js" type="text/javascript"&gt;&lt;/script&gt;'' to your HTML5 file. his doesn''t necessarily need to go into the head of your file. Since your web browser will chronologically process the HTML5 and script in the order it is presented, if you have ''global'' function or reference elements that have not yet been processed than the browser will throw an error. It doesn''t know that the element you are referencing is below the script element. It may be safe to put your script element below your HTML5 content or try to design a system where this wouldnt be an issue.\n </para><para>\n There are a few basics that we will be covering in this tutorial which will include how to common knowledge with Javascript, call functions, and trigger events.\n </para>', 4),
(8, 'Common Javascript Elements and Concepts', '<para>\n There are a few main objects and methods that would be excellent to understand as an introduction to Javascript. Before listing some of them, it should be noted that Javascript behaves similarly to python in that it does not explicitly define an element''s/object''s type. You do not need to specifiy the parameter type (ie. function(nameOfParam){} rather than function(int name){}) or need to specifying one for a variable. You can simply give the type ''var'' for every variable you create (similar to the capabilities of C#). With that in mind, here is a list of some common Javascript knowledge:\n </para><definition term="Document">\n The ''document'' object represents the HTML5 document object. This gives you access to all of the elements found in the file. These are known as the Document Object Model (DOM) which we will later discuss how to get elements and attributes for these objects.\n </definition><definition term="Methods of DOM">\n Similar to the concept of a class object, DOM objects have attributes and methods which can be called. For example if we want to write a line to the document, the method ''writeln()'' can be called.\n </definition><code>document.writeln("Hello World!")</code><definition term="Attributes of DOM">\n Objects have attributes that can be set or simply just to get the value of an attribute. You can call the method ''.setattribute(...)'' or to modify/get CSS attributes you can directly set them. For example if you want to hide an element you can do the following\n </definition><code>myClass.style.display = ''none'';</code><definition term="Semi-colon">\n The semi colon is not required but it is greatly advised to reduce any bugs that may occur\n </definition><definition term="Case Sensitive">\n Javascript is case sensitive so be sure to have the correct casing!\n </definition><definition term="Quotes">\n You can mix and match single quotes '' with double quotes " and they should work the same in any case. What is useful is when you want to display either single/ double quotes to the user. You should then nest the quotes you wish to show in the opposing quotes.\n </definition><definition term="Window">\n The window object can be thought of as the browser window. You can invoke an alert dialog (a), create a function that will be called when the window loads (b), and even get a user''s input from a window prompt (c). We will discuss this syntax later in the tutorial.\n </definition><code>(a) window.alert("Warning!")</code><code>(b) window.onload() = function() {};</code><code>(c) window.prompt("Please enter a number");</code><definition term="Concatinating Vs. Adding">\n The ''+'' symbol can be used to concatinate strings as well as add numbers. You must be careful with this and not confuse concatinating string with adding numbers. Look at the following as an example, where y = 5.\n <code>y + 2 =" + y + 2</code>\n <code>Expected: "y + 2 = 7"</code>\n <code>Result: "y + 2 = 52"</code>\n This is the wrong result since we mixed string with integer values. We need to specify exactly that we want to add two integers by grouping them within brackets. This will add (y + 2) as ints then concat them with the "y + 2 =" string.\n <code>y + 2 =" + (y + 2)</code>\n <code>Result: "y + 2 = 7"</code>\n </definition><definition term="Strict Equals/Not Equals">\n Typically it is good enough to compare two objects/values with a == a or a != b. But in Javascript the following condition would also return true, "72" == 72, even though one is a string and another is an integer. To strictly compare you must use ''==='' or ''!==''\n </definition><code>"72" === 72 will result in false</code><definition term="If Condition">\n You can use if, else if, and else as you would with any other programming language.\n </definition><code>if(condition){}else if(condition){} else{};</code><definition term="While Loops">\n You can loop until a condition is met with\n </definition><code>while(condition){};</code><definition term="For Loops">\n A for loop allows you to iterate through an indexed array or list.\n </definition><code>for(...){}</code><definition term="Increment, Decrement">\n For integers, you can easilly increment or decrement them with the following\n </definition><image src="../static/img/fig7-13_p239.png">\n Figure 2. Javascript Increment &amp; Decrement\n </image>', 4),
(9, 'Function', '<para>You can create functions in Javascript that will help you group together common code with parameters. For example the basic structure is:\n </para><code>function AddTwo(input) { return input + 2; }</code><para>\n You can also use common function such as many Math functions. To list a few:\n </para><code>Math.pow(2,3) is 2 to the power of 3</code><code>Math.random() returns a random number</code><code>Math.floor(2.33), Math.ceil(2.99), Math.round(2.5) will round your values</code><para>\n You can retrieve HTML5 elements by their id, class, etc.\n </para><code>\n document.getElementById("idVal") or using jquery $("#idVal") to retrieve an element by their ID\n </code><code>\n document.getElementsByClassName("classVal") or using jquery $(".classVal") to get elements by their class\n </code><para>\n You can also have recursive functions (function that call itself) or iterative functions.\n </para>', 4),
(10, 'Event Handling', '<para>\n Buttons, forms, inputs, and various other HTML5 elements can trigger events! Javascript allows you to control what happens when they are triggered. You can either use a inline functions, global elements, or use JQuery to invoke these methods.\n </para><definition term="Inline">\n In your HTML5 element you can set the event method to call a javascript method you have written.\n </definition><image src="../static/img/inline_event.png">\n Figure 3. Inline Javascript\n </image><definition term="Global">\n You can retrieve the element and then use their event handling method in a global way\n </definition><image src="../static/img/global_event.png">\n Figure 4. Global Element\n </image><definition term="JQuery">\n If you use JQuery, you can use a shorter form than having to globally retrieve the element first\n </definition><image src="../static/img/jquery_event.png">\n Figure 5. Using JQuery\n </image>', 4),
(11, 'Canvas', '<para>\n Below is an example of the canvas element (Detail p.446)\n </para><image src="../static/img/fig14-2_p446.png">\n Figure 6. Code for a Canvas Element\n </image><para>\n There is so much you can do with the canvas element so it would be best to explore <a href="https://www.w3schools.com/html/html5_canvas.asp">here</a>!\n </para><conclusion>\n This concludes the tutorial on Javascript and HTML5 Canvas. Please try out the quiz to test out your knowledge on this unit.\n </conclusion>', 5),
(12, 'XML Basics', '<para>\n There are a few basic definitions and structures in XML that are handy to know!\n </para><definition term="Data/Text Content">\n As seen in the above example, John is considered to be the data of the document\n </definition><definition term="Element">\n In the above example, firstName is an element. This will link the element to its contained data. Note that an XML file should always contain one root element (ie. player) and element names should not contain any whitespace. It is important to include a root element, match each start tag with an end tag, and to keep casing uniform since XML is case sensitive\n </definition><definition term="Nested Elements">\n You can nest elements within each other to create a more detailed and complex XML structure. You should declare your XML version similar to how you declare the information for an HTML5 file. To do this you should follow what''s written at line 1 of the example above.\n </definition><definition term="Type">\n You can add a type attribute to your XML elements which can help differentiate between, for example, contact elements where one is of type sender and one is of type receiver.\n </definition><definition term="Namespace">\n Often times there may be elements that you want to be represented with the same name. Even though XML allows this, it can be hard in terms of readability and maintainability. You can use namespaces to provide some organization.\n </definition><para>\n You should always ensure your XML is well formed. There are many online resources such as <a href="https://www.w3schools.com/xml/xml_validator.asp">W3Schools</a> to validate your XML.\n </para><para>\n Most XML files can be viewed in a browser without any styling but will usually have a warning at the top to state no style is associated with it. Although you can still view the XML it''s not in a nice format that the browser can display. You can add a XSL sheet linked to your XML (similar to the idea of a CSS file to an HTML5 file). <a class="def">XSL</a> stands for Extensible Stylesheet Language and will be explained later.\n </para>', 6),
(13, 'Document Type Definition (DTD)', '<definition term="DTD">\n This stands for Document type definition. It describes the structure of your XML file so that an XML parser can verify if your XML document is valid. This will help when it comes to formatting your XML in a valid and uniform way. XML documents that do not follow the linked DTD document will display an error. Although you have a well structured document, you may not have a valid document. However, DTDs have been considered not flexible enough and do not specify data types. This is where XML schemas come in.\n </definition>', 6),
(14, 'XML Schema', '<definition term="XSD">\n stands for XML Schema Document. This also describes the elements and content of your XML document with the added information of data types. XSD are more widely used to validate XML Documents.\n </definition>', 6),
(15, 'Styling XML with XSL', '<para>\n As mentioned above, XSL files specifies how a browser should render the XML file. This will help us control what elements are headings, paragraphs, or lists! The line below should be added into your XML file to link your .xsl file.\n </para><code>&lt;?xml-stylesheet href="resume.xsl" type="text/xsl"?&gt;</code><para>\n The following definitions introduce some basic knowledge with XSL:\n </para><definition term="Template">\n Templates are used in XSL files to match and specify what nodes to process. The syntax is as follows\n </definition><code>&lt;xsl:template match = "element"&gt;</code><definition term="Root Element">\n match ="/"\n </definition><definition term="Specific Element">\n match ="nameOfElement"\n </definition><definition term="Any Element">\n match ="*"\n </definition><definition term="Current Element">\n match =".", note this should work best within a nested match\n </definition><para>\n The content of an XSL file is very similar to an HTML5 but its content are the XML values. The following is an example of how you can set up a XSL to style your XML documents (Detail p.540).\n </para><image src="../static/img/fig15-19_p540.png">\n XSL Styling\n </image>', 6),
(16, 'Common AJAX Definitions', '<para>\n Ajax is commonly used through XMLHttpRequests, which was mentioned earlier to be request manager objects. It can detect state changes such as onreadystatechange to ensure that the data requests has been fully sent from the server. The following are some other common XMLHttpRequest methods\n </para><definition term="send()">\n This can sent get, post, etc. to the server and specify the data to retreive\n </definition><definition term="responseXML">\n Retrieves the xml file from the server\n </definition><definition term="abort()">\n Stops the current request\n </definition><definition term="status">\n A status = 200 means a sucessful request was done. 500 means an error has occured\n </definition><para>\n This is just a basic run down of Ajax and as always I reccommend to go online to find more detailed things you can do with Ajax. W3Schools does a good job <a href="https://www.w3schools.com/xml/ajax_intro.asp">here</a>!\n </para><conclusion>\n This concludes the tutorial on XML and Ajax. Please try out the quiz to test out your knowledge on this unit.\n </conclusion>', 7);''')

conn.commit()
print ("sections Records Insert successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS `units` (
  `ID` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `Title` varchar(225) NOT NULL,
  `Overview` text
);''')
conn.commit()
print ("Table units created successfully")

conn.execute('''INSERT INTO `units` (`ID`, `Title`, `Overview`) VALUES
(1, 'Unit 1: HTML6 & CSS3', '<para>\n For Unit 1, you will be introduced to the main concepts of the web and the basic structure to writing in HTML5 &amp; CSS3. The following information has been sourced from Athabasca University COMP 466 and Internet and World Wide Web How To Program, 5th Edition (Deitel, Harvey, Abbey Deitel).\n </para><para>\n Following the completion of this tutorial, a quiz to test your knowledge will be available.\n </para>'),
(2, 'Unit 2: JavaScript & HTML5 Canvas', '<para>\n For Unit 2, you will be introduced to the main concepts and basic structure to JavaScript (not to be confused with Java). The following information has been sourced from Athabasca University COMP 466 and Internet and World Wide Web How To Program, 5th Edition (Deitel, Harvey, Abbey Deitel).\n </para><para>\n Following the completion of this tutorial, a quiz to test your knowledge will be available.\n </para>'),
(3, 'Unit 3: XML & Ajax', '<para>\n This unit will teach you the basics of XML and Ajax. These can help organize your documents and data as well as provide ways to request the server for information.\n </para>');''')

conn.commit()
print ("units Records Insert successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS `users` (
  `username` varchar(225) PRIMARY KEY NOT NULL,
  `password` varchar(225) NOT NULL
);''')
conn.commit()
print ("Table users created successfully")

conn.execute('''INSERT INTO `users` (`username`, `password`) VALUES
('root', 'root'),
('111', '111111');''')
conn.commit()
print ("users Records Insert successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS `userLearn` (
  `username` varchar(225) NOT NULL,
  `UnitID` INTEGER NOT NULL,
  `chapter` INTEGER NOT NULL
);''')
conn.commit()
print ("Table userLearn created successfully")

conn.execute('''INSERT INTO `userLearn` (`username`, `UnitID`, `chapter`) VALUES
('root', '1', '1');''')

conn.commit()
print ("userLearn Records Insert successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS `userQuiz` (
  `username` varchar(225) NOT NULL,
  `UnitID` INTEGER NOT NULL,
  `score` INTEGER NOT NULL
);''')
conn.commit()
print ("Table userQuiz created successfully")