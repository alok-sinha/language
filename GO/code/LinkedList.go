package main

import (
	"fmt"
)

type Node struct {
	item int
	next *Node
}

type LinkedList interface {
	Create () *interface{}
	Add (interface{}) *interface{}
	Delete(interface{}) *interface{}
}

func (Node) Create() *Node {
	var head *Node = nil
	return head
}

func (head *Node) Add (i int) *Node {
	var tmp  = new(Node)
	tmp.item = i
	tmp.next = head
	return tmp
}

func main() {
	
	

	var head *Node = nil

	for i:=0; i < 5; i++ {
		if head == nil {
			head = new(Node)
			head.item = i
			head.next = nil
		} else {
			tmp := new(Node)
			tmp.item = i
			tmp.next = head
			head = tmp
		}
	}

	head = head.Add(6)
	var node = head
	for ;node != nil;  {
		fmt.Print(node.item, " ")
		node = node.next
	}

	var l LinkedList = *head

	l = l.Add(7)
	node = l
	for ;node != nil;  {
		fmt.Print(node.item, " ")
		node = node.next
	}
}
