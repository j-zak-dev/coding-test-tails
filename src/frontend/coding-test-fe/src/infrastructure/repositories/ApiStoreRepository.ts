import type { Store, RichStore } from '../../domain/aggregates/Store'
import type { StoreInterface } from '../../domain/interfaces/storeInterface'
import type { RichStoreApiDTO, StoreApiDTO } from '../dtos/StoreApiDTO'
import { mapStoreApiDtoToDomain, mapStoreNameToBackend } from '../mappers/storeMapper'

export class ApiStoreRepository implements StoreInterface {
    private apiUrl: string

    constructor(apiUrl: string) {
        this.apiUrl = apiUrl
    }

    async getAll(): Promise<Store[]> {
        const response = await fetch(`${this.apiUrl}/stores`)
        if (!response.ok) {
            throw new Error('Failed to fetch stores')
        }

        const data = (await response.json()) as StoreApiDTO[]
        return data.map(mapStoreApiDtoToDomain)
    }

    async searchByName(name: string): Promise<Store[]> {
        name = mapStoreNameToBackend(name)
        const response = await fetch(`${this.apiUrl}/stores/search_by_name/${name}`)
        if (!response.ok) {
            throw new Error('Failed to search stores by name')
        }

        const data = (await response.json()) as StoreApiDTO[]
        return data.map(mapStoreApiDtoToDomain)
    }

    async getEnrichedByName(name: string): Promise<RichStore[]> {
        name = mapStoreNameToBackend(name)
        const params = new URLSearchParams({ name })
        const response = await fetch(`${this.apiUrl}/stores/enriched_search_by_name?${params.toString()}`)
        if (!response.ok) {
            throw new Error('Failed to search enriched stores by name')
        }

        const data = (await response.json()) as RichStoreApiDTO[]
        return data.map(mapStoreApiDtoToDomain)
    }
} 