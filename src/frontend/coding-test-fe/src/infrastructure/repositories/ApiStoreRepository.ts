import type { Store } from '../../domain/aggregates/Store'
import type { StoreInterface } from '../../domain/interfaces/storeInterface'
import type { StoreApiDTO } from '../dtos/StoreApiDTO'
import { mapStoreApiDtoToDomain } from '../mappers/storeMapper'

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

    async searchByPostalCode(postalCode: string): Promise<Store[]> {
        const response = await fetch(`${this.apiUrl}/stores/search_by_postcode/${postalCode}`)
        if (!response.ok) {
            throw new Error('Failed to search stores by postal code')
        }

        const data = (await response.json()) as StoreApiDTO[]
        return data.map(mapStoreApiDtoToDomain)
    }

    async searchByName(name: string): Promise<Store[]> {
        const response = await fetch(`${this.apiUrl}/stores/search_by_name/${name}`)
        if (!response.ok) {
            throw new Error('Failed to search stores by name')
        }

        const data = (await response.json()) as StoreApiDTO[]
        return data.map(mapStoreApiDtoToDomain)
    }
}