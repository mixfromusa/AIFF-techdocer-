# object pattern (abstract)

TODO: describe:
- type.complex;
- type.pattern;
- type.simple: string, set, array, date, abstract, linked_list;
- rules.common: object, abstract (example: [version](Standarts\versioning-structure.md)).

Meta:
- object.name: abstract.object.name.pattern
- object.type: abstract.objects.types.set
- object.description: "A pattern for creating and validating objects in a common rules that is independent of the class of objects"
- objects.fields.required.set: {
    - object.name : string;
    - object.type : abstract.types.set;
    - object.date.created : date;
    - object.date.updated : date;
    - object.version : complex.[version](Standarts\versioning-structure.md)};
- object.fields.optional.set: {
	- object.description : linked_list.string};
- object.methods.abstract.actions.set : abstact.actions.types.set;
- object.methods.requared.set: {
    - object.create (constructor) : object;
    - object.update (updater): result(object.updating);
    - object.read (reader): result(object.reading);
    - object.delete (deleter): result(object.deleting);
	- object.description.update (descriptor.param.list) : linked_list.string;
	- object.validate (validator.pattern): object}
- object.rules.required.set: {
	- object.rule.naming : rule.naming.object;
	- object.rule.versioning : [rule.versioning.object](Standarts\versioning-structure.md);
	- object.rule.descriptioning : rule.descriptioning.object;
	- object.rule.validation : rule.validation.object;
	- object.rule.dating : rule.dating.object;
	- object.rule.deleting : rule.deleting.object