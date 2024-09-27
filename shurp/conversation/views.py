from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from .forms import ConversationMessageForm
from .models import Conversation

@login_required
# new conversation view
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    # Prevent user from starting a conversation with their own item
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    # Check if a conversation already exists between the user and the item owner
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        # Redirect to the first existing conversation
        return redirect('conversation:detail', pk=conversations.first().pk)

    # If the request method is POST, handle form submission
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            # Create a new conversation
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            # Create and save the first conversation message
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            # Redirect to the item detail page after the conversation is created
            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    # Render the conversation form if the request method is GET or the form is invalid
    return render(request, 'conversation/new.html', {
        'form': form
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })   