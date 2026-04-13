import type { Store } from '../../domain/aggregates/Store'
import type { StoreApiDTO } from '../dtos/StoreApiDTO'

export function mapStoreApiDtoToDomain(dto: StoreApiDTO): Store {
  return {
    name: dto.name,
    postalCode: dto.postcode,
    coordinates: {
      latitude: dto.latAndLong[0],
      longitude: dto.latAndLong[1],
    },
  }
}
