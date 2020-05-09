from pycaprio.core.objects.curation import Curation
from pycaprio.core.schemas.curation import CurationSchema


def test_curation_schema_dump_one_dict_many_false(curation_schema: CurationSchema,
                                                  deserialized_curation: Curation,
                                                  serialized_curation: dict):
    assert curation_schema.dump(deserialized_curation) == serialized_curation


def test_curation_schema_dump_one_dict_many_true(curation_schema: CurationSchema,
                                                 deserialized_curation: Curation,
                                                 serialized_curation: dict):
    assert curation_schema.dump([deserialized_curation], many=True) == [serialized_curation]
