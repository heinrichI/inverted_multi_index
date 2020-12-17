//
// Created by dima on 08.04.17.
//
#include "../catch/catch.hpp"
#include "../../src/distance/SubspacesProductEuclideanDistanceComputer.h"
#include "../../src/util/array_utils.h"


TEST_CASE("using SubspacedVectors compute subspace distances from query_vector to base_vectors[4,2,2]",
          "[distance][subspace][SubspacedVectors][SubspacesProductEuclideanDistanceComputer]") {

    const int subspaces_count = 2;
    const int subspace_base_vectors_count = 4;
    const int subspace_vector_dim = 2;
    SubspacedVectors<float> subspacedVectors(subspaces_count, subspace_base_vectors_count, subspace_vector_dim);
    REQUIRE(subspacedVectors.getTotalComponentsCount() == 16);

    float subspace_base_vectors[16] = {1, 2, 3, 4, 5, 6, 7, 8,
                                                                               3, 4, 0, 0, 1, 2, 1, 2};
    subspacedVectors.setSubspacedVectors(subspace_base_vectors);


    SubspacesProductEuclideanDistanceComputer<float> subspacesProductEuclideanDistanceComputer(subspacedVectors);
    const int distances_count_ = subspacedVectors.getTotalVectorsCount();
#define distances_count_CONST 8
    REQUIRE(distances_count_ == distances_count_CONST);
    std::vector<float> right_answer_vector = {5, 25, 61, 113,
                                              0, 25, 8, 8};

    float query_vector[subspaces_count * subspace_vector_dim] = {0, 0,
                                                                 3, 4};
    SECTION("raw array") {
        float subspace_distances[distances_count_CONST];
        subspacesProductEuclideanDistanceComputer.computeSquaredDistances(query_vector, subspace_distances);
        std::vector<float> answer_vector = array_to_vector(subspace_distances, distances_count_);
        REQUIRE(answer_vector == right_answer_vector);
    }

    SECTION("SubspacedVectors") {
        SubspacedVector<float> subspacedQueryVector(subspaces_count, subspace_vector_dim);
        SubspacedScalars<float> *subspacedDistances = SubspacedScalars<float>::allocateOneDimSubspacedVectors(
                subspacedVectors);
        subspacedQueryVector.setSubspacedVectors(query_vector);
        subspacesProductEuclideanDistanceComputer.computeSquaredDistances(subspacedQueryVector, *subspacedDistances);
        std::vector<float> answer_vector = array_to_vector(subspacedDistances->subspaced_vectors, distances_count_);
        REQUIRE(answer_vector == right_answer_vector);
    }
}
