#! /usr/bin/python
def rec(prod,var,stack):
	for k in var :	
		stack.append(k)
		if k>='A' and k<='Z':
			for i in prod[k]:
				 rec(prod,i,stack)
		else:
			h=1
	return stack 
	
def prod(var,pro):
	prod= dict()
	for i in var:
		prod[i]=pro[i]
	return prod
def print_production(pro):
	for i in pro.keys():
		r = pro[i]
		print i,'->',
		for j in r:
			if j == r[-1]:
				print j
			else:
				print j,'|',
productions = dict()
terminals = []
variables = []
pro = "something"
while(pro!="$"):
	pro = raw_input()
	l = list(pro)
	for i in l:
		if i>='a' and i<='z':
			if i not in terminals:
				terminals.append(i)
		elif i>='A' and i<='Z':
			if i not in variables:
				variables.append(i)
	try:
		l = pro.split('->')[0]
	except:
		print 'Invalid Production'
		exit()
	try:
		r = pro.split('->')[1].split('|')
		if productions.has_key(l):
			v = list(productions[l])
		else:
			v = []
		for i in r:
			if i not in v:
				v.append(i)
		productions[l] = v
	except:
		pass
print '\nGiven Grammar:'
print '\nTerminals :'
print terminals
print '\nvariables:'
print variables
print '\nProductions:'
print_production(productions)
print '\nNew Grammer:'
stack=list()
stack=rec(productions,variables[0],stack)
ter=list()
var=list()
for i in stack:
		if i>='A' and i<='Z':
			if i not in var:
				var.append(i)
		if i>='a' and i<='z':
			if i not in ter:
				ter.append(i)
print '\nTerminals :'
print ter 
print '\nvariables:'
print var 
print '\nProductions  :'
pro=dict()
prod=prod(var,productions)
print_production(prod)
