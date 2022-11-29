# simplified version
from django.shortcuts import get_object_or_404, render

from sesame.decorators import authenticate

@authenticate(scope="chat_profile:{pk}")
def share_profile(request, pk):
    chat_profile = get_object_or_404(request.user.chatprofile_set, pk=pk)
    return render(request, "chat_profile/share_chatprofile.html", {"chat_profile": chat_profile})


"""
# extended version
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render

import sesame.utils

# Since I don specify related_name=… [Django-doc] for the ForeignKey from Notification to User, the default name is modelname_set (chatprofile_set)
def share_profile(request, pk):
    customer = sesame.utils.get_user(request, scope=f"chat_profile:{pk}")
    print("customer: ", customer)
    if customer is None:
        raise PermissionDenied
    chat_profile = get_object_or_404(customer.chatprofile_set, pk=pk)
    return render(request, "chat_profile/share_chatprofile.html", {"chat_profile": chat_profile})
"""
