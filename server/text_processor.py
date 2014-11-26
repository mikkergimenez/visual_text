from practnlptools.tools import Annotator
import re


class TextProcessor:

    objects = []

    def assign_objects(self, fragment):
        for a, b in fragment.items():
            if re.match("A[0-9]+", a):
                clean_b = re.sub(r'the |a ', r'', b.lower())
                if clean_b.lower() not in self.objects:
                    self.objects.append(clean_b.lower())
            print self.objects

    def get_item(self, word):
            if (word):
                iconArrayLarge = ['cat', 'cats']
                iconArraySmall = ['kitten', 'kittens']
                processes = ['step', 'steps']
                if word in iconArrayLarge:
                    return '<a href="https://en.wikipedia.org/wiki/Cat"><img height=50px src="images/cat.png"></a>'
                elif word in iconArraySmall:
                    return '<a href="https://en.wikipedia.org/wiki/kitten"><img height=30px src="images/cat.png"></a>'
                elif word in processes:
                    return '<a class="btn btn-lg btn-default" href="https://en.wikipedia.org/wiki/' + word + '">' + word + '</a>'
                else:
                    pass
            else:
                return 'item'

    def process(self, text):
        annotator = Annotator()
        tokens = annotator.getAnnotations(text)
        chunks = tokens['chunk']
        ner = tokens['ner']
        pos = tokens['pos']
        srl = tokens['srl']
        words = tokens['words']

        for part in srl:
            self.assign_objects(part)
        
        returnCode = ""
        print self.objects
        for object in self.objects:
            print self.get_item(object)
            if self.get_item(object) is not None:
                returnCode += str(self.get_item(object))

        return returnCode

'''
    


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

textProcessor = TextProcessor()

app.get '/process_words', (req, res) ->
    res.header 'Access-Control-Allow-Origin', '*'
    res.send { text: textProcessor.process(req.param('text')) }
'''
