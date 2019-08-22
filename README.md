# lyric-profile

give a singer's name and find if his or her lyric is positive or negative


## Example command
```
(venv) ➜  lyric-profile git:(master) python cli.py --name="Jason Mraz"
Jason Mraz's songs are more positive


(venv) ➜  lyric-profile git:(master) ✗ python cli.py --name="eminem"   
eminem's songs are more negative

```

### notice
please run following code to download nltk dictionaries first.
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')

```
have fun! nice day
