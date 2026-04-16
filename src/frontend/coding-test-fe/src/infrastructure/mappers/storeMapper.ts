import type { RichStore, Store } from '../../domain/aggregates/Store'
import type { RichStoreApiDTO, StoreApiDTO } from '../dtos/StoreApiDTO'

export function mapStoreApiDtoToDomain(dto: StoreApiDTO): Store {
  return {
    name: dto.name.replace(/_/g, ' '),
    postalCode: dto.postcode,
  }
}

export function mapRichStoreApiDtoToDomain(dto: RichStoreApiDTO): RichStore {
  return {
    name: dto.name.replace(/_/g, ' '),
    postalCode: dto.postcode,
    coordinates: {
      latitude: dto.latAndLong[0],
      longitude: dto.latAndLong[1],
    },
  }
}

export function mapStoreNameToBackend(name: string): string {
  return name.replace(/ /g, '_')
}