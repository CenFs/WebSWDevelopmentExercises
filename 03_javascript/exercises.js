// keywordusage('Dive Into Python is a free book for experienced programmers', ['Python', 'python', 'scala'])
// [true, false, false]
function keywordusage(text, keywords) {
  var words = text.split(' ');
  for (i = 0; i < keywords.length; i++) {
    for (j = 0; j < words.length; j++) {
      if (words[j] == keywords[i]) {
        keywords[i] = true;
        break;
      }
    }
  }
  for (i = 0; i < keywords.length; i++) {
    if (keywords[i] != true) keywords[i] = false;
  }
  return keywords;
}

// frequencies('foo foo bar foo   bar buz', ['foo', 'bar'])
// {"bar": 2, "foo": 3}
function frequencies(text, wordlist) {
  var words = text.split(' ');
  var dict = {};
  for (i = 0; i < wordlist.length; i++) {
    count = 0;
    for (j = 0; j < words.length; j++) {
      if (wordlist[i] == words[j]) {
        count++;
      }
    }
    dict[wordlist[i]] = count;
  }
  return dict;
}


function rotate(a) {
  var tmp = a[a.length - 1]
  for (i = a.length - 1; i > 0; i--) {
    a[i] = a[i - 1];
  }
  a[0] = tmp;
  return a;
}

function rotate(a, step) {
  while (step >= a.length) {
    step -= a.length;
  }
  while (step < 0) {
    step += a.length;
  }
  if (step == 0) {
    return a;
  } else {
    while (step--) {
      var tmp = a[a.length - 1]
      for (i = a.length - 1; i > 0; i--) {
        a[i] = a[i - 1];
      }
      a[0] = tmp;
    }
    return a;
  }
}
