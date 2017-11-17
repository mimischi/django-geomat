"""Serializers for REST framework"""
from rest_framework import serializers

from geomat.stein.models import CrystalSystem, Handpiece, MineralType, Photograph, Classification, QuizQuestion,\
    QuizAnswer, Cleavage, GlossaryEntry


class StdImageField(serializers.ImageField):
    """
    Get all the variations of the StdImageField
    """

    def to_native(self, obj):
        return self.get_variations_urls(obj)

    def to_representation(self, obj):
        return self.get_variations_urls(obj)

    def get_variations_urls(self, obj):
        """
        Get all the logo urls.
        """

        # Initiate return object
        return_object = {}

        # Get the field of the object
        field = obj.field

        # A lot of ifs going araound, first check if it has the field variations
        if hasattr(field, 'variations'):
            # Get the variations
            variations = field.variations
            # Go through the variations dict
            for key in variations.keys():
                # Just to be sure if the stdimage object has it stored in the obj
                if hasattr(obj, key):
                    # get the by stdimage properties
                    field_obj = getattr(obj, key, None)
                    if field_obj and hasattr(field_obj, 'url'):
                        # store it, with the name of the variation type into our return object
                        return_object[key] = super(
                            StdImageField, self).to_representation(field_obj)

        # Also include the original (if possible)
        if hasattr(obj, 'url'):
            return_object['original'] = super(StdImageField,
                                              self).to_representation(obj)

        return return_object


class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ('classification_name', 'mineral_type')


class NameClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ('classification_name',)


class CleavageSerializer(serializers.ModelSerializer):
    cleavage = serializers.SerializerMethodField()

    class Meta:
        model = Cleavage
        fields = ("cleavage", "coordinates")

    def get_cleavage(self, obj):
        return obj.get_cleavage_display()


class MineralTypeSerializer(serializers.ModelSerializer):
    classification = NameClassificationSerializer()
    systematics = serializers.SerializerMethodField()
    fracture = serializers.SerializerMethodField()
    cleavage = CleavageSerializer(many=True)
    lustre = serializers.SerializerMethodField()
    display_name = serializers.SerializerMethodField()
    # chemical_formula = serializers.SerializerMethodField()

    class Meta:
        model = MineralType
        fields = '__all__'
        depth = 1

    def get_systematics(self, obj):
        return obj.get_systematics_display()

    def get_fracture(self, obj):
        lst = []
        choice_dict = dict(obj.FRACTURE_CHOICES)
        if obj.lustre:
            for choice in obj.fracture:
                lst.append(choice_dict.get(choice))
        return lst

    def get_cleavage(self, obj):
        lst = []
        choice_dict = dict(obj.CLEAVAGE_CHOICES)
        if obj.cleavage:
            for choice in obj.cleavage:
                lst.append(choice_dict.get(choice))
        return lst

    def get_lustre(self, obj):
        lst = []
        choice_dict = dict(obj.LUSTRE_CHOICES)
        if obj.lustre:
            for choice in obj.lustre:
                lst.append(choice_dict.get(choice))
        return lst

    def get_display_name(self, obj):
        return obj.variety if obj.variety else obj.minerals
        # def get_chemical_formula(self, obj):
        #     return "`" + obj.chemical_formula + "`"

    # This is a first aproache to provide pictures for a Mineraltype
    # Yet this is to be revisioned since not only a few Minerals have more than one handpiece
    # but also a few of the handpieces have more than one photograph

    # def get_images(self, obj):
    #     images =[]
    #     if obj.handpiece_count >1:
    #         for handpiece in obj.handpiece_set.all():
    #             images.append(StdImageField(handpiece.photograph.image_file))
    #     else:
    #         images.append(StdImageField(obj.handpiece_set.get().photograph.get().image_file))


class MineralProfilesSerializer(MineralTypeSerializer):

    image_file = serializers.SerializerMethodField()
    IMAGE_DICT = {
        # Min : #Photo
        1: 34, 2: 31, 3: 32, 4: 35, 5: 36, 6: 37, 7: 139, 8: 47, 9: 99, 10: 40,
        11: 44, 12: 98, 13: 41, 14: 151, 15: 97, 16: 131, 18: 134, 19: 135,
        20: 132, 21: 133, 22: 144, 25: 48, 26: 113, 28: 117, 29: 122, 30: 140, 31: 74,
        34: 50, 35: 146, 36: 49, 37: 54, 38: 150, 39: 51, 40: 52, 41: 56, 42: 59, 44: 60,
        46: 61, 48: 63, 49: 64, 50: 67, 51: 65, 52: 68, 53: 77, 54: 79, 55: 80, 56: 75, 57: 69,
        58: 70, 59: 71, 60: 143, 61: 123, 62: 72, 63: 73, 64: 101, 66: 137, 67: 136, 68: 141,
        69: 102, 70: 82, 71: 81, 83: 84, 84: 85, 85: 145, 86: 112, 87: 104, 88: 138, 89: 108,
        90: 111, 91: 114, 92: 114, 93: 107, 96: 129, 97: 119, 98: 120, 99: 116, 100: 128,
        101: 105, 102: 109, 104: 29, 105: 124, 106: 125, 107: 126, 108: 127, 114: 153,
        115: 154, 116: 162,
    }

    def get_image_file(self, obj):
        if obj.pk in MineralProfilesSerializer.IMAGE_DICT.keys():
            photo_pk = MineralProfilesSerializer.IMAGE_DICT[obj.pk]
            photo = Photograph.objects.only("image_file").get(pk=photo_pk)
            return StdImageField().to_representation(obj=photo.image_file)
        return {}


class CrystalSystemSerializer(serializers.ModelSerializer):
    mineral_type = MineralTypeSerializer()

    class Meta:
        model = CrystalSystem
        fields = ('id', 'mineral_type', 'crystal_system', 'temperature',
                  'pressure')


class HandpieceSerializer(serializers.ModelSerializer):
    mineral_type = MineralTypeSerializer(many=True)

    class Meta:
        model = Handpiece
        fields = ('id', 'name', 'mineral_type', 'finding_place',
                  'current_location', 'old_inventory_number', 'created_at',
                  'last_modified')


class PhotographSerializer(serializers.ModelSerializer):
    image_file = StdImageField()
    handpiece = HandpieceSerializer()
    online_status = serializers.BooleanField()

    class Meta:
        model = Photograph
        fields = ('id', 'image_file', 'handpiece', 'orientation', 'shot_type',
                  'online_status', 'created_at', 'last_modified')

# some things have to be cleared out before work can continue

# class ProfileSerializer(MineralTypeSerializer):
#     images = serializers.SerializerMethodField()
#
#     def get_images(self, obj):
#         pass

class QuizAnswerLessSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizAnswer
        fields = ('id', 'atext', 'correct', 'feedback_correct', 'feedback_incorrect')


class QuizQuestionLessSerializer(serializers.ModelSerializer):
    qtype = serializers.SerializerMethodField()

    class Meta:
        model = QuizQuestion
        fields = ('id', 'qtext', 'qtype', 'tags', 'difficulty')

    def get_qtype(self, obj):
        choice_dict = dict(obj.QTYPE_CHOICES)
        return choice_dict.get(obj.qtype)


class QuizAnswerFullSerializer(serializers.ModelSerializer):
    question = QuizQuestionLessSerializer()

    class Meta:
        model = QuizAnswer
        fields = '__all__'


class QuizQuestionFullSerializer(serializers.ModelSerializer):
    qtype = serializers.SerializerMethodField()
    answers = QuizAnswerLessSerializer(many=True)

    class Meta:
        model = QuizQuestion
        fields = '__all__'

    def get_qtype(self, obj):
        choice_dict = dict(obj.QTYPE_CHOICES)
        return choice_dict.get(obj.qtype)


class GlossaryEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = GlossaryEntry
        fields = '__all__'
