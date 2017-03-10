function addPersonMethods(object) {
  var person = object;
  person.greet = function (greetingString) {
    console.log(greetingString + ", my name is " + person.name);
  };
  person.compareAge = function (anotherPersonObject) {
    if (person.age > anotherPersonObject.age) {
      console.log("My name is " + person.name + " and I'm older than " + anotherPersonObject.name);
    } else if (person.age < anotherPersonObject.age) {
      console.log("My name is " + person.name + " and I'm younger than " + anotherPersonObject.name);
    } else {
      console.log("My name is " + person.name + " and I'm equally young as " + anotherPersonObject.name);
    }
  };
  person.namesake = function (anotherPersonObject) {
    if (person.name == anotherPersonObject.name) {
      console.log("We have the same name, " + anotherPersonObject.name + " and I!");
    } else {
      console.log("We have different names, " + anotherPersonObject.name + " and I.");
    }
  };
  return person;
};
