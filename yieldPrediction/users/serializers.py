from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """A Serializer for user.models.User"""

    class Meta:
        model = User
        # Specific the model attributes needed for serialization
        fields = ['id', 'email', 'password', 'firstName', 'lastName']
        # Prevents password from being read
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """Creates new User from validated data.

        Overrites existing create function from ModelSerializer. This
        is used indirectly via the serializer.save method.  
        
        Args:
            validated_data (dict): Dictionary of user information. 

        Returns:
            users.models.User : The newly created User object. 
        """
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


    def update(self, instance, validated_data):
        """Updates an existing Users information.

        Overrites existing create function from ModelSerializer. This
        is used indirectly via the serializer.save method.  
        
        Args:
            instance (users.models.User): The User whos information needs to be updated.
            validated_data (dict): Dictionary of user information. 

        Returns:
            users.models.User : The newly created User object. 
        """
        email = validated_data.get('email')
        password = validated_data.get('password')
        firstName = validated_data.get('firstName')
        lastName = validated_data.get('lastName')

        if email is not None:
            instance.email = email 
        if password is not None:
            instance.set_password(password)
        if firstName is not None:
            instance.firstName = firstName
        if lastName is not None:
            instance.lastName = lastName
        instance.save()
        return instance
