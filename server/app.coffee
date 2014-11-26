express = require 'express'
natural = require 'natural'
pos     = require 'pos'
app = express()

class TextProcessor
    get_item: (text) ->
        if (text)
            iconArrayLarge = ['cat', 'cats']
            iconArraySmall = ['kitten', 'kittens']
            processes = ['step', 'steps']
            if ($.inArray(text, iconArrayLarge) not -1)
                return '<a href="https://en.wikipedia.org/wiki/Cat"><img height=50px src="images/cat.png"></a>'
            else if ($.inArray(text, iconArraySmall) not -1)
                return '<a href="https://en.wikipedia.org/wiki/kitten"><img height=30px src="images/cat.png"></a>'
            else if ($.inArray(text, processes) not -1)
                return '<a class="btn btn-lg btn-default" href="https://en.wikipedia.org/wiki/' + text + '">' + text + '</a>'
        else
            return 'item'


    process: (text)->
        # var re = /There are ([0-9]) layers in (the|a) ([.*])/
    
        returnVal = '<ul>'
        #for i in found[2]
        #    returnVal += '<li class="list-unstyled">' + get_item(found[3]) + '</li>'
        #returnVal += '</ul>'
        console.log text
        words = new pos.Lexer().lex(text)
        console.log words
        taggedWords = new pos.Tagger().tag(words)
        for i in taggedWords
            taggedWord = i
            console.log taggedWord
            returnVal += '<li class="list-unstyled">' + taggedWord[0] + '. ' + taggedWord[1] + '</li>'
        
        returnVal += '</ul>'

        return returnVal

textProcessor = new TextProcessor()

app.get '/process_words', (req, res) ->
    res.header 'Access-Control-Allow-Origin', '*'
    res.send { text: textProcessor.process(req.param('text')) }

server = app.listen(3000, () ->
    console.log 'Listening on port %d', server.address().port
)
