#include <stdio.h>
#include <stdlib.h>
#define MAX 10

// Stack implementation
int s[MAX], top = -1, n = MAX;

__declspec(dllexport) int push(int val)
{
    if (top == n - 1) {
        return -1;
    } else {
        top++;
        s[top] = val;
        return 0;
    }
}

__declspec(dllexport) int pop() {
    if (top == -1) {
        return -1;
    } else {
        int val = s[top];
        top--;
        return val;
    }
}

__declspec(dllexport) int* get_stack(int *size) {
    *size = top + 1;
    return s;
}

// Queue implementation


// Linked List implementation
struct node
{int val;
struct node*next ;
};
struct node*head=NULL,*p,*q,*nw;

__declspec(dllexport) int ins_beg()
{
	int x;
	printf("Enter x: ");
	scanf("%d",&x);
	nw = (struct node *) malloc (sizeof(struct node));
	nw -> val = x;
	nw -> next = NULL;
	
	if(head = NULL)
	{
		head = nw;
	}
	else
	{
		nw -> next = head;
		head = nw;
	}
	return 1;
}

__declspec(dllexport) int ins_end()
{
	int x;
	printf("Enter x: ");
	scanf("%d",&x);
	nw = (struct node *) malloc (sizeof(struct node));
	nw -> val = x;
	nw -> next = NULL;
	
	if(head = NULL)
	{
		head = nw;
	}
	else
	{
		p = head;
		while(p -> next != NULL)
		{
			p = p -> next;
		}
		p -> next = nw;
	}
	return 1;
}

__declspec(dllexport) int ins_pos()
{
	int x,pos,c = 0;
	printf("Enter x: ");
	scanf("%d",&x);
	printf("Enter position: ");
	scanf("%d",&pos);
	nw = (struct node *) malloc (sizeof(struct node));
	nw -> val = x;
	nw -> next = NULL;
	
	if(head = NULL)
	{
		head = nw;
	}
	else
	{
		p = head;
		while(c < pos - 1 && p != NULL)
		{
			q = p;
			p = p -> next;
			c++;
		}
		q -> next = nw;
		nw -> next = p;
	}
    return 1;
}

__declspec(dllexport) int del_beg()
{
	if(head == NULL)
	{
		printf("\nLinked List is Empty");
	}
	else
	{
		p = head;
		head = p->next;
		free(p);
		printf("\nValue Deleted\n");
	}
}

__declspec(dllexport) int del_end()
{
	if(head == NULL)
	{
		printf("\nLinked List is Empty");
	}
	else
	{
		p = head;
		while(p->next != NULL)
		{
			q = p;
			p = p -> next;
		}
		q -> next = NULL;
		free(p);
		printf("\nValue Deleted\n");
	}
}

__declspec(dllexport) int del_pos()
{
	int pos,c = 0;
	printf("Enter position: ");
	scanf("%d",&pos);	
	if(head = NULL)
	{
		printf("\nLinked List is Empty");
	}
	else
	{
		p = head;
		while(c < pos - 1)
		{
			q = p;
			p = p -> next;
			free(p);
		}
	}
	printf("\nValue Deleted\n");
}

__declspec(dllexport) void display()
{
	if(head == NULL)
	{
		printf("\nLinked List is empty");
	}
	else
	{
		printf("\nThe Linked List is: ");
		p = head;
		while(p != NULL)
		{
			printf("%d -->\n", p -> val);
			p = p -> next;
		}
	}
}